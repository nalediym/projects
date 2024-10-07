import os
from Parser import Parser
from CodeWriter import CodeWriter

class VMTranslator:
    def __init__(self, input_file):
        """
        Initializes the VMTranslator with the input file.
        Arguments:
            input_file: Path to the input file
        Output:
            An assembly file named the same as the input file but with the .vm extension replaced with .asm
        """
        self.input_file: os.PathLike = input_file

        if not self.input_file.endswith('.vm'):
            raise ValueError(f"Input file must have a .vm extension: {self.input_file}")

        # Constructs a Parser to handle the input file  
        self.parser: Parser = Parser(self.input_file)
        # Constructs a CodeWriter to handle the output file
        self.output_file: os.PathLike = self.input_file.replace('.vm', '.asm')
        # self.code_writer: CodeWriter = CodeWriter(self.output_file)
        # self.output_file_lines: list[str] = []

    def translate(self):
        """
        Drives the translation process.
        Iterates through the input file, parsing each line and generating code from it, using the services of the Parser and a CodeWriter.

        """
        # Construct a Parser to handle the input file
        self.parser = Parser(self.input_file)
        
        # Construct a CodeWriter to handle the output file
        self.output_file: os.PathLike = self.input_file.replace('.vm', '.asm')
        self.code_writer = CodeWriter(self.output_file)
        
        # Iterate through the input file, parsing each line and generating code
        self.output_file_lines: list[str] = []
        while self.parser.has_more_lines():
            
            command_type = self.parser.commandType()
            assembly_code = ""
            
            # Handle different command types and generate code
            if command_type == 'C_ARITHMETIC':
                assembly_code = self.code_writer.writeArithmetic(self.parser.arg1()) # writes add, sub, neg, eq, gt, lt, and, or, not to output file
            elif command_type == 'C_PUSH' or command_type == 'C_POP':
                assembly_code = self.code_writer.writePushPop(command_type, self.parser.arg1(), self.parser.arg2())
            
            self.output_file_lines.append(assembly_code)
            self.parser.advance()
        # Write the output file
        with open(self.output_file, 'w') as file:
            file.write('\n'.join(self.output_file_lines))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 vm_translator.py fileName.vm")
    else:
        translator = VMTranslator(sys.argv[1])
        translator.translate()