import os
import re

A_INSTRUCTION = "A_INSTRUCTION" # e.g. @100 
C_INSTRUCTION = "C_INSTRUCTION" # e.g. D=D+A
L_INSTRUCTION = "L_INSTRUCTION" # e.g. (LOOP)

VALID_COMMAND_TYPES = [A_INSTRUCTION, C_INSTRUCTION, L_INSTRUCTION]
# VALID_DEST_FIELDS = ["M", "D", "MD", "A", "AM", "AD", "AMD"]
# VALID_COMP_FIELDS = ["0", "1", "-1", "D", "A", "!D", "!A", "-D", "-A", "D+1", "A+1", "D-1", "A-1", "D+A", "D-A", "A-D", "D&A", "D|A", "M", "!M", "-M", "M+1", "M-1", "D+M", "D-M", "M-D", "D&M", "D|M"]
# VALID_JUMP_FIELDS = ["JGT", "JEQ", "JGE", "JLT", "JNE", "JLE", "JMP"]

class Parser:
    """Encapsulates access to the input code. Reads an assembly language command, parses it, and provides
    convenient access to the command's components (fields and symbols). In addition, removes all white space and comments.
    """

    def __init__(self, input_file):
        """
        Opens the input file and gets ready to parse it.

        Args:
            input_file (str): The path to the input .asm file.
        Attributes:
            input_file (os.PathLike): The path to the input .asm file.
            current_instruction (str): The current instruction being parsed. eg: "@100" or "D=D+A" or "(LOOP)"
        """
        self.input_file : os.PathLike = input_file
        self.current_instruction : str = None
        self.current_line_number : int = 0
        self.instructions : list[str] = []
        self.current_instruction_index : int = 0 # Index of the current instruction in the list of self.instructions

        # Open the input file and read all the lines
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"File {self.input_file} does not exist")
        with open(self.input_file, "r") as file:
            self.instructions = file.readlines()

        # TODO: use __enter__ and __exit__ to open and close the file and read the lines 


    def hasMoreLines(self) -> bool:
        """
        Checks if there is more work to do

        Returns:
            bool: True if there are more lines, False otherwise.
        """
        return self.current_instruction_index < len(self.instructions)

    def advance(self):
        """
        Reads the next command from the input and makes it the current command.
        Should be called only if hasMoreLines() is true.
        Initially there is no current command.
        """
        # Read the next command
        self.current_instruction = self.instructions[self.current_instruction_index]
        self.current_instruction_index += 1

    def instructionType(self):
        """
        Returns the type of the current command:
        A_INSTRUCTION for @Xxx where Xxx is either a symbol or a decimal number
        C_INSTRUCTION for dest=comp;jump
        L_INSTRUCTION (actually, pseudo-command) for (Xxx) where Xxx is a symbol

        Returns:
            str: The type of the current command (A_INSTRUCTION, C_INSTRUCTION, or L_INSTRUCTION).
        """
        # 1. Check if the current command is an A_INSTRUCTION
        if self.current_instruction.startswith("@"): 
            return A_INSTRUCTION
        # 2. Check if the current command is an L_INSTRUCTION
        elif self.current_instruction.startswith("(") and self.current_instruction.endswith(")"):
            return L_INSTRUCTION
        # 3. Check if the current command is a C_INSTRUCTION   
        elif re.match(r"^[AMD]*=[01!-]*[AMD01!-]*;J[A-Z]*$", self.current_instruction):
            return C_INSTRUCTION
        else:  
            raise ValueError("Invalid instruction")

    def symbol(self):
        """
        Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx).
        Should be called only when command_type() is A_INSTRUCTION or L_INSTRUCTION.

        Returns:
            str: The symbol or decimal Xxx of the current command.
        """
        # 1. Check if the current command is an A_INSTRUCTION 
            # Return decimal Xxx of the current command   
        if self.instructionType() == A_INSTRUCTION:
            pass
        # 2. Check if the current command is an L_INSTRUCTION
            # Return the symbolof the current command
        elif self.instructionType() == L_INSTRUCTION:
            pass    
        else:
            raise ValueError(f"Invalid instruction type: {self.instructionType()}. Must be A_INSTRUCTION or L_INSTRUCTION") 

    def _contains_dest_field(self):
        """
        Checks if the current instruction contains a dest field.

        Returns:
            bool: True if the current instruction contains a dest field, False otherwise.
        """
        return "=" in self.current_instruction
        
    def dest(self):
        """
        Returns the dest mnemonic in the current C-INSTRUCTION (8 possibilities).
        Should be called only when command_type() is C_INSTRUCTION.

        Returns:
            str: The dest mnemonic in the current C-INSTRUCTION.
        """
        # Return the dest mnemonic in the current C-INSTRUCTION
        # 1. Check if the current command is a C_INSTRUCTION
        if self.instructionType() == C_INSTRUCTION:
            # 2. Return the dest mnemonic in the current C-INSTRUCTION
            if self._contains_dest_field():
                return self.current_instruction.split("=")[0].strip()
            else:
                return "null"
        else:
            raise ValueError(f"Invalid instruction type: {self.instructionType()}. Must be C_INSTRUCTION")


    def comp(self):
        """
        Returns the comp mnemonic in the current C-INSTRUCTION (28 possibilities).
        Should be called only when command_type() is C_INSTRUCTION.

        Returns:
            str: The comp mnemonic in the current C-INSTRUCTION.
        """
        # Return the comp mnemonic in the current C-INSTRUCTION
        # 1. Check if the current command is a C_INSTRUCTION
        if self.instructionType() == C_INSTRUCTION:
            # 2. Return the comp mnemonic in the current C-INSTRUCTION
            if self._contains_dest_field() and self._contains_jump_field():
                dest, comp, jump = re.split('=|;', self.current_instruction)
                return comp.strip()
            elif self._contains_dest_field():
                return self.current_instruction.split("=")[1].split(";")[0].strip()
            elif self._contains_jump_field():
                return self.current_instruction.split(";")[0].strip()
            else:
                raise ValueError(f"Invalid instruction: {self.current_instruction}. Must contain either dest or jump field.")
        else:
            raise ValueError(f"Invalid instruction type: {self.instructionType()}. Must be C_INSTRUCTION")

    def _contains_jump_field(self):
        """
        Checks if the current instruction contains a jump field.

        Returns:
            bool: True if the current instruction contains a jump field, False otherwise.
        """
        return ";" in self.current_instruction
        
    def jump(self):
        """
        Returns the jump mnemonic in the current C-INSTRUCTION (8 possibilities).
        Should be called only when command_type() is C_INSTRUCTION.

        Returns:
            str: The jump mnemonic in the current C-INSTRUCTION.
        """
        # Return the jump mnemonic in the current C-INSTRUCTION
        # 1. Check if the current command is a C_INSTRUCTION
        if self.instructionType() == C_INSTRUCTION:
            # 2. Return the jump mnemonic in the current C-INSTRUCTION
            if self._contains_jump_field():
                return self.current_instruction.split(";")[1].strip()
            else:
                return "null"
        else:
            raise ValueError(f"Invalid instruction type: {self.instructionType()}. Must be C_INSTRUCTION")
    