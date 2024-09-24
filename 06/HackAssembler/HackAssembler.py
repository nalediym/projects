#!/usr/bin/env python3

from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable
import os

from typing import Callable

def decimal_to_binary(num):
    return f'{num:016b}'

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

        # Get the first instruction
        self.parser.advance()
        if self.parser.current_instruction_index != 0:
            raise ValueError("Error Initializing Parser: Current instruction index is not 0. Must start at the beginning of the file")



    def _validate_input_file(self):
        """
        Validate the input file
        """
        if not os.path.isfile(self.input_file):
            raise FileNotFoundError(f"File {self.input_file} not found")
        if not self.input_file.endswith('.asm'):
            raise ValueError("Invalid file extension. Please provide a .asm file.")
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"File {self.input_file} not found")    
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

        self.parser.current_instruction = ""
        self.current_line_number = 0
        self.parser.current_instruction_index = 0 

        # Check if the parser has more lines to process
        if not self.parser.hasMoreLines():
            raise ValueError("Error Resetting Parser: No more lines to process")

    def assemble(self):
        """
        Main assembly logic goes here
        Creates the output file
        """
        self.first_pass()
        self._reset_parser()
        self.second_pass()

    
    def _sanitize_instructions(self) -> Callable[[str], str]:
        """
        Clean the instructions by removing comments and white spaces,
        and removing any lines that are entirely comments.
        Preserves the order of non-comment instructions.
        """
        # Define the lambda function
        clean_and_filter = lambda instruction: instruction.strip() if instruction.strip() and not instruction.strip().startswith("//") else ""
        
        # Use filter with the lambda function
        return clean_and_filter

    def first_pass(self):
        """
        First pass of the assembly

        Reads the program lines, one by one
        focusing only on (label) declarations.
        Adds the found labels to the symbol table
        """

        self.parser.instructions = list(filter(bool, map(self._sanitize_instructions(), self.parser.instructions)))

        # Iterate over the instructions and process each one
        line_num_counter = 0
        for instruction in self.parser.instructions:
            # Check the type of instruction
            if instruction.instructionType() == Parser.L_INSTRUCTION:
                # It's a label declaration
                label_symbol = instruction.symbol()
                self.symbol_table.addEntry(label_symbol, line_num_counter)
            line_num_counter += 1

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
            if instruction.instructionType() == Parser.A_INSTRUCTION:
                a_symbol = instruction.symbol()
                if not self.symbol_table.contains(a_symbol):
                    self.symbol_table.addEntry(a_symbol, self.parser.current_instruction_index)
                address = self.symbol_table.getAddress(a_symbol) 
                # Convert the address from decimal to binary
                binary_value = decimal_to_binary(address)
            elif instruction.instructionType() == Parser.C_INSTRUCTION:
                dest, comp, jump = instruction.dest(), instruction.comp(), instruction.jump()
                binary_value = Code.comp(comp) + Code.dest(dest) + Code.jump(jump)
            else:
                raise ValueError(f"Invalid instruction type: {instruction.instructionType()}")

            self.output_file_lines.append(binary_value)

        with open(self.output_file_name, "w") as file:
            file.write("\n".join(self.output_file_lines))
                

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python HackAssembler.py <input_file.asm>")
        sys.exit(1)

    assembler = HackAssembler(sys.argv[1])
    assembler.assemble()