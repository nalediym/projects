#!/usr/bin/env python3


from parser import Parser
from code_writer import CodeWriter
import os

class VMTranslator:
    def __init__(self, input_file):
        """
        Initializes the VMTranslator with the input file.
        """
        self.input_file: os.PathLike = input_file
        self.parser: Parser = None
        self.code_writer: CodeWriter = None
        self.output_file: os.PathLike = None

    def translate(self):
        """
        Drives the translation process.
        """
        # Construct a Parser to handle the input file
        self.parser = Parser(self.input_file)
        
        # Construct a CodeWriter to handle the output file
        self.output_file: os.PathLike = self.input_file.replace('.vm', '.asm')
        self.code_writer = CodeWriter(self.output_file)
        
        # Iterate through the input file, parsing each line and generating code
        # TODO: convert to a with statement? 
        while self.parser.has_more_lines():
            self.parser.advance()
            command_type = self.parser.command_type()
            
            # Handle different command types and generate code
            if command_type == 'C_ARITHMETIC':
                self.code_writer.write_arithmetic(self.parser.arg1()) # writes add, sub, neg, eq, gt, lt, and, or, not to output file
            elif command_type == 'C_PUSH' or command_type == 'C_POP':
                self.code_writer.write_push_pop(command_type, self.parser.arg1(), self.parser.arg2())
        # Close the output file
        self.code_writer.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python vm_translator.py fileName.vm")
    else:
        translator = VMTranslator(sys.argv[1])
        translator.translate()