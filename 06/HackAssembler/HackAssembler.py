#!/usr/bin/env python3

from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable
import os


class HackAssembler:
    """
    Opens the input file (Prog.asm) and gets ready to process it 
    Constructs a symbol table, and adds to it all the predefined symbols
    """
    def __init__(self, input_file: os.PathLike):
        self.parser = Parser(input_file)
        self.code = Code()
        self.symbol_table = SymbolTable()
        self.output_file_name : str = input_file.replace('.asm', '.hack')
        self.output_file : os.PathLike = None


    def assemble(self):
        """
        Main assembly logic goes here
        Creates the output file
        """
        self.first_pass()
        self.second_pass()

    def first_pass(self):
        """
        First pass of the assembly

        Reads the program lines, one by one
        focusing only on (label) declarations.
        Adds the found labels to the symbol table
        """
        pass

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
        pass

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python HackAssembler.py <input_file.asm>")
        sys.exit(1)

    assembler = HackAssembler(sys.argv[1])
    assembler.assemble()