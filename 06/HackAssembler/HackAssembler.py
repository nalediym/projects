#!/opt/homebrew/bin/python3 


from .Parser import Parser
from .Code import Code
from .SymbolTable import SymbolTable

import os

from typing import Callable

def decimal_to_binary(num: int) -> str:
    return f'{num:016b}'

A_INSTRUCTION = "A_INSTRUCTION" # e.g. @100 
C_INSTRUCTION = "C_INSTRUCTION" # e.g. D=D+A
L_INSTRUCTION = "L_INSTRUCTION" # e.g. (LOOP)

class HackAssembler:
    """
    Opens the input file (Prog.asm) and gets ready to process it 
    Constructs a symbol table, and adds to it all the predefined symbols
    """
    def __init__(self, input_file: os.PathLike):
        self.output_file_name : str = input_file.replace('.asm', '.hack')
        self.output_file : os.PathLike = None
        self.output_file_lines : list[str] = []

        # Open the input file with the Parser
        self.parser = Parser(input_file)
        # Validate the input file
        self._validate_input_file()

        # Construct a symbol table and add all the predefined symbols
        self.symbol_table = SymbolTable()
        self.code = Code()
        if self.parser.current_instruction_index != 0:
            raise ValueError("Error Initializing Parser: Current instruction index is not 0. Must start at the beginning of the file")

        # Check if there are any instructions before advancing
        if self.parser.hasMoreLines():
            self.parser.advance()
        else:
            raise ValueError("Error: Input file is empty or contains no valid instructions")

    def _validate_input_file(self):
        """
        Validate the input file
        """
        if not os.path.isfile(self.parser.input_file):
            raise FileNotFoundError(f"File {self.parser.input_file} not found")
        if not self.parser.input_file.endswith('.asm'):
            raise ValueError("Invalid file extension. Please provide a .asm file.")
        if not os.path.exists(self.parser.input_file):
            raise FileNotFoundError(f"File {self.parser.input_file} not found")    
    def _validate_output_file(self):
        """
        Validate the output file
        """
        if os.path.exists(self.output_file_name):
            raise FileExistsError(f"File {self.output_file_name} already exists")

    def _reset_parser(self):
        """
        Reset the parser to the beginning of the file before generating binary code with second pass
        """

        self.parser.current_instruction = "" # Reset the current instruction
        self.parser.current_instruction_index = 0 # Reset the current instruction index

        # Check if the parser has more lines to process
        if not self.parser.hasMoreLines():
            raise ValueError("Error Resetting Parser: No more lines to process. Parser should have more lines to process.")

    def assemble(self):
        """
        Main assembly logic goes here
        Creates the output file
        """
        self.first_pass()
        self._reset_parser()
        self.second_pass()
    
    # def _sanitize_instructions(self):
    #     sanitized = []

    #     for instruction in self.parser.instructions:
    #         # Remove leading/trailing whitespace
    #         instruction = instruction.strip()
            
    #         # Skip empty lines
    #         if not instruction:
    #             continue
            
    #         # Skip lines that are only comments
    #         if instruction.startswith('//'):
    #             continue
    #         # Remove inline comments
    #         if '//' in instruction:
    #             instruction = instruction.split('//')[0].strip()
            
    #         # Add non-empty, non-comment instructions to the sanitized list
    #         if instruction:
    #             sanitized.append(instruction)
        
    #     self.parser.instructions = sanitized

    def first_pass(self):
        """
        First pass of the assembly

        Reads the program lines, one by one
        focusing only on (label) declarations.
        Adds the found labels to the symbol table
        """
        # Iterate over the instructions and process each one
        line_num_counter = 0
        while self.parser.hasMoreLines():
            # Check the type of instruction
            if self.parser.instructionType() == L_INSTRUCTION:  
                # It's a label declaration
                label_symbol = self.parser.symbol()
                if not self.symbol_table.contains(label_symbol):
                    self.symbol_table.addEntry(label_symbol, line_num_counter)
            line_num_counter += 1
            self.parser.advance()

    def second_pass(self):
        """
        Second pass of the assembly
        
        (starts again from the beginning of the file)
        While there are more lines to process:
            Gets the next instruction, and parses it
            If the instruction is  @ symbol 
                If symbol is not in the symbol table, adds it to the table
                Translates the symbol into its binary value
            If the instruction is  dest =comp ; jump
                Translates each of the three fields into its binary value
            Assembles the binary values into a string of sixteen 0’s and 1’s
            Writes the string to the output file.
        """
        while self.parser.hasMoreLines():
            self.parser.advance()
            instruction = self.parser.current_instruction
            if self.parser.instructionType() == A_INSTRUCTION:
                a_symbol = self.parser.symbol()
                if not self.symbol_table.contains(a_symbol):
                    
                    self.symbol_table.addEntry(a_symbol, int(a_symbol))
                address : int= self.symbol_table.getAddress(a_symbol) 
                # Convert the address from decimal to binary
                binary_value = decimal_to_binary(address)
                if len(binary_value) != 16:
                    raise ValueError(f"Invalid binary value {len(binary_value)} for A-instruction: {instruction}")
                if binary_value[0] != "0":
                    raise ValueError(f"Invalid binary value {binary_value[0]} for A-instruction: {instruction}")
            elif self.parser.instructionType() == C_INSTRUCTION:
                dest, comp, jump = self.parser.dest(), self.parser.comp(), self.parser.jump()
                # binary_value = self.code.comp(comp) + self.code.dest(dest) + self.code.jump(jump)
                if dest is None: 
                    raise ValueError(f"Invalid dest field {dest} for instruction: {instruction}")
                if comp is None:
                    raise ValueError(f"Invalid comp field {comp} for instruction: {instruction}")
                if jump is None:
                    raise ValueError(f"Invalid jump field {jump} for instruction: {instruction}")
                comp_binary = self.code.comp(comp)  
                dest_binary = self.code.dest(dest)
                jump_binary = self.code.jump(jump)
                if len(comp_binary) != 7:
                    raise ValueError(f"Invalid comp binary value {comp_binary} for instruction: {instruction}")
                if dest_binary is None or len(dest_binary) != 3:
                    raise ValueError(f"Invalid dest binary value {dest_binary} for instruction: {instruction}")
                if len(jump_binary) != 3:
                    raise ValueError(f"Invalid jump binary value {jump_binary} for instruction: {instruction}")
                binary_value = "111" + comp_binary + dest_binary + jump_binary
            elif self.parser.instructionType() == L_INSTRUCTION:
                pass # Do nothing with L_INSTRUCTION it will be processed in the first pass
            else:
                raise ValueError(f"Invalid instruction type for instruction: {instruction}")

            if len(binary_value) != 16:
                raise ValueError(f"Invalid binary value {len(binary_value)} for instruction: {instruction}")
            self.output_file_lines.append(binary_value)

        self._validate_output_file()    

        with open(self.output_file_name, "w") as file:
            file.write("\n".join(self.output_file_lines))
    
    def _validate_output_file(self):
        """
        Validate the output file has instructions to output 
        """
        if self.output_file_lines == []:
            raise ValueError(f"No instructions to output: {self.output_file_lines}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python HackAssembler.py <input_file.asm>")
        sys.exit(1)

    assembler = HackAssembler(sys.argv[1])
    assembler.assemble()