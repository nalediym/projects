import os
from dataclasses import dataclass
from vm_templates import VMTemplates, TemplateType, PushTemplate, PopTemplate, ArithmeticTemplate

COMMAND_ASM_MAP = {
    'add': 'M=D+M',
    'sub': 'M=M-D',
    'neg': 'M=-M',
    'eq': 'D;JEQ',
    'gt': 'D;JGT',
    'lt': 'D;JLT',
    'and': 'M=D&M',
    'or': 'M=D|M',
    'not': 'M=!M',    
}

STANDARD_SYMBOL_VM_MAP = {
    'SP' : 0, 
    'LCL': 1, 
    'ARG': 2, 
    'THIS': 3, 
    'THAT': 4,
    'SCREEN': 16384, 
    'KBD': 24576, 
    **{f'R{i}': i for i in range(0, 24576)}
}

SEGMENT_SYMBOL_MAP = {
    'local': 'LCL',
    'argument': 'ARG',
    'this': 'THIS',
    'that': 'THAT',
    'constant': 'CONSTANT',
    'static': 'STATIC',
    'pointer': 'SP',
}

STATIC_SYMBOL_TEMPLATE = "{filename_without_extension}.{index}"
@dataclass
class Segment:
    """
    Represents a memory segment in the VM. ex: local, argument, this, that, constant, static, pointer, or temp
    """
    name: str # ex: local, argument, this, that, constant, static, pointer, or temp
    index: int # ex: 0, 1, 2, 3, 4, etc.
    symbol: str # ex: LCL, ARG, THIS, THAT, SCREEN, KBD, etc.

    def __int__(self):
        return self.index

class CodeWriter:
    """
    Generates assembly code from parsed VM commands
    Translates VM commands into Hack assembly code.

    Attributes:
        segment_symbol_map (dict): Maps VM memory segments to their symbolic names.
        output_file_name (str): Name of the output assembly file.
        output (file): File object for writing the generated assembly code.
    """
    def __init__(self, output_file: os.PathLike):
        """
        Opens up the output file / stream and gets ready to write into it.
        Args:
            output_file (str): The name of the output file to write assembly code.
        """
        self.segment_symbol_map = SEGMENT_SYMBOL_MAP
        self.output_file_name = os.path.basename(output_file)
        self.output_file = output_file
        self.output = None
        self.command_handlers = {
            PushTemplate.COMMAND.value: self._write_push,
            PopTemplate.COMMAND.value: self._write_pop,
            ArithmeticTemplate.COMMAND.value: self._write_arithmetic,
        }

    def __enter__(self):
        self.output = open(self.output_file, 'w')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.output:
            self.output.close()

    def _write_push(self, segment: str, index: int) -> str:
        template = PushTemplate(segment)
        return VMTemplates.get_template(TemplateType.PUSH, template)({'index': index}) + '\n'

    def _write_pop(self, segment: str, index: int) -> str:
        template = PopTemplate(segment)
        return VMTemplates.get_template(TemplateType.POP, template)({'index': index}) + '\n'

    def _write_arithmetic(self, command: str) -> str:
        template = ArithmeticTemplate(command)
        return VMTemplates.get_template(TemplateType.ARITHMETIC, template)({}) + '\n'

    def write_command(self, command_type: str, arg1: str = None, arg2: int = None) -> None:
        handler = self.command_handlers.get(command_type)
        if handler:
            if command_type == ArithmeticTemplate.COMMAND.value:
                self.output.write(handler(arg1))
            else:
                self.output.write(handler(arg1, arg2))
        else:
            raise ValueError(f"Unknown command type: {command_type}")

    def write_arithmetic(self, command):
        """
        Writes to the output file the assembly code that implements the given arithmetic-logical command.
        Args:
            command (str): The arithmetic command (add, sub, neg, eq, gt, lt, and, or, not).
        """
        # Implement the logic to write assembly code for arithmetic operations
        self.output.write(f"{command}\n")

    def write_pop(self, segment: str, integer: int):
        """
        Writes to the output file the assembly code that implements the given pop command.
        Args:
            segment (str): The memory segment to operate on.
            index (int): The index in the memory segment.
        """
        if segment.name == 'constant':
            pass # do nothing (see p.22)
        elif segment.name in ['local', 'argument', 'this', 'that']:
            pass
        elif segment.name == 'temp':
            pass
        elif segment.name == 'static':
            pass
        else:
            raise ValueError(f"Invalid segment: {segment.name}. Must be constant, local, argument, this, that, temp, or static")


    def write_push(self, segment: str, index: int):
        """
        Writes to the output file the assembly code that implements the given push or pop command.
        Args:z
            command (str): Either C_PUSH or C_POP.
            segment (str): The memory segment to operate on ( e.g. local, argument, this, that, constant, static, pointer, or temp)
            index (int): The index in the memory segment.
        """
        if segment.name == 'constant':
            self.output.write(f"@{index}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
        elif segment.name in ['local', 'argument', 'this', 'that']:
            pass
        elif segment.name == 'temp':
            pass
        elif segment.name == 'static':
            pass
        else:
            raise ValueError(f"Invalid segment: {segment.name}. Must be constant, local, argument, this, that, temp, or static")

    def write_push_pop(self, command: str, segment: str, index: int):
        """
        Writes to the output file the assembly code that implements the given push or pop command.
        Args:z
            command (str): Either C_PUSH or C_POP.
            segment (str): The memory segment to operate on ( e.g. local, argument, this, that, constant, static, pointer, or temp)
            index (int): The index in the memory segment.
        """
        # Implement the logic to write assembly code for push/pop operations
        segment = Segment(name=segment, index=index, symbol=self.segment_symbol_map[segment])
        if command == 'C_PUSH':
            self.write_push(segment)
        elif command == 'C_POP':
            self.write_pop(segment)
        else:
            raise ValueError(f"Invalid command: {command}. Must be C_PUSH or C_POP")
    def close(self):
        """
        Closes the output file.
        """
        if self.output:
            self.output.close()

