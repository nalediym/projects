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
        # Initialize other necessary attributes


    def hasMoreLines(self) -> bool:
        """
        Checks if there is more work to do

        Returns:
            bool: True if there are more lines, False otherwise.
        """
        pass

    def advance(self):
        """
        Reads the next command from the input and makes it the current command.
        Should be called only if has_more_commands() is true.
        Initially there is no current command.
        """
        # Read the next command
        pass

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

    def dest(self):
        """
        Returns the dest mnemonic in the current C-INSTRUCTION (8 possibilities).
        Should be called only when command_type() is C_INSTRUCTION.

        Returns:
            str: The dest mnemonic in the current C-INSTRUCTION.
        """
        # Return the dest mnemonic in the current C-INSTRUCTION
        # 1. Check if the current command is a C_INSTRUCTION
        # 2. Return the dest mnemonic in the current C-INSTRUCTION
        pass

    def comp(self):
        """
        Returns the comp mnemonic in the current C-INSTRUCTION (28 possibilities).
        Should be called only when command_type() is C_INSTRUCTION.

        Returns:
            str: The comp mnemonic in the current C-INSTRUCTION.
        """
        # Return the comp mnemonic in the current C-INSTRUCTION
        pass

    def jump(self):
        """
        Returns the jump mnemonic in the current C-INSTRUCTION (8 possibilities).
        Should be called only when command_type() is C_INSTRUCTION.

        Returns:
            str: The jump mnemonic in the current C-INSTRUCTION.
        """
        # Return the jump mnemonic in the current C-INSTRUCTION
        pass
    