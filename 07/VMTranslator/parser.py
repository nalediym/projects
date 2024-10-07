import os

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

COMMAND_TYPE_MAP: dict[str, str] = {
    # Push and Pop commands
    'push': 'C_PUSH',
    'pop': 'C_POP',
    # Arithmetic / Logical commands 
    'add': 'C_ARITHMETIC',
    'sub': 'C_ARITHMETIC',
    'neg': 'C_ARITHMETIC',
    'eq': 'C_ARITHMETIC',
    'gt': 'C_ARITHMETIC',
    'lt': 'C_ARITHMETIC',
    'and': 'C_ARITHMETIC',
    'or': 'C_ARITHMETIC',
    'not': 'C_ARITHMETIC',
    # Branching commands
    'label': 'C_LABEL',
    'goto': 'C_GOTO',
    'if-goto': 'C_IF',
    # Function commands
    'function': 'C_FUNCTION',
    'return': 'C_RETURN',
    'call': 'C_CALL',
}
class Parser:
    """
    Parses a VM command and returns the command type.
    """
    def __init__(self, input_file: os.PathLike):
        """
        Opens the input file and gets ready to parse it.
        :param input_file: Path to the input file
        """
        self.input_file = input_file
        self.validate_input_file()
        self.lines: list[str] = []
        self.current_line_number: int = 0
        self.current_instruction: str = ""
        with open(input_file, 'r') as file:
            for line in file.readlines():
                line = line.strip()

                if not line.startswith('//'):
                    # Remove comments
                    line = line.split('//')[0].strip()
                    if line:
                        self.lines.append(line)

        if self.has_more_lines():
            self.current_instruction = self.lines[self.current_line_number]

    def validate_input_file(self):
        """
        Validates the input file.
        Raises FileNotFoundError if the file doesn't exist.
        Raises ValueError if the file doesn't have a .vm extension.
        """
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"File not found: {self.input_file}")
        if not self.input_file.lower().endswith('.vm'):
            raise ValueError(f"Input file must have a .vm extension: {self.input_file}")


    def has_more_lines(self) -> bool:
        """
        Are there more lines in the input?
        Returns: boolean
        """

        return self.current_line_number < len(self.lines) - 1

    def advance(self) -> None:
        """
        Reads the next command from the input and makes it the current command.
        Should be called only if has_more_lines() is true.
        """
        if self.has_more_lines():
            self.current_line_number += 1
            self.current_instruction = self.lines[self.current_line_number]
            logger.debug(f"Current instruction: {self.current_instruction}")

    def commandType(self) -> str:
        """
        Returns a constant representing the type of the current command.
        Returns: "C_ARITHMETIC" | "C_PUSH" | "C_POP" | "C_LABEL" | "C_GOTO" | "C_IF" | "C_FUNCTION" | "C_RETURN" | "C_CALL"
        rtype: str
        """
        command = self.current_instruction.split()[0] # eg: push, pop, add, sub, etc.
        command_type = COMMAND_TYPE_MAP.get(command, None)
        if command_type is None:
            raise ValueError(f"Invalid command. No valid command type found for: {self.current_instruction}")
        return command_type
    
    def arg1(self) -> str:
        """
        Returns the first argument of the current command. In the case of C_ARITHMETIC, the command itself
        (add, sub, etc.) is returned. Should not be called if the current command is C_RETURN.
        Returns: string
        """
        command_type = self.commandType()

        if command_type == 'C_ARITHMETIC':
            command = self.current_instruction.split()[0] # eg: push, pop, add, sub, etc.
            return command # add, sub, etc.
        elif command_type == 'C_RETURN':
            raise ValueError(f"arg1() should not be called if the current command is C_RETURN")
        elif command_type in ('C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL'):
            arg_1 = self.current_instruction.split()[1] # eg: push local 3 ---> local
            return arg_1 # local, argument, this, that, etc.
        else:
            raise ValueError(f"Invalid command: {self.current_instruction}")

    def arg2(self) -> int:
        """
        Returns the second argument of the current command. Should be called only if the current command
        is C_PUSH, C_POP, C_FUNCTION, or C_CALL.
        Returns: int 
        """
        command_type = self.commandType() 
        if command_type in ('C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL'):
            arg2 = self.current_instruction.split()[2] # eg: push local 3 ---> 3
            if arg2.isdigit():
                return int(arg2) 
            else:
                raise ValueError(f"{arg2} should only be integer")
        else:
            raise ValueError(f"arg2() should only be called if the current command is C_PUSH, C_POP, C_FUNCTION, or C_CALL, not {command_type}")
        

