import os
import sys
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
        # open the input file
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"File not found: {input_file}")
        # Check if the input file has a .vm extension
        if not input_file.lower().endswith('.vm'):
            raise ValueError(f"Input file must have a .vm extension: {input_file}")
        with open(input_file, 'r') as file:
            self.lines: list[str] = file.readlines()
        
        self.validate_lines() # validate the lines in the file
        
        self.current_line: int = 0
        self.current_instruction: str = None


    def validate_lines(self):
        """
        Validates the lines in the file.
        """
        for line in self.lines:
            if '//' in line:
                line = line.split('//')[0].strip()
            if not line:
                self.lines.remove(line)
    def has_more_lines(self):
        """
        Are there more lines in the input?
        Returns: boolean
        """
        return self.current_line < len(self.lines)

    def advance(self):
        """
        Reads the next command from the input and makes it the current command.
        Should be called only if has_more_lines() is true.
        """
        if self.has_more_lines():
            self.current_line += 1
            self.current_instruction = self.lines[self.current_line]

    def command_type(self) -> str:
        """
        Returns a constant representing the type of the current command.
        Returns: "C_ARITHMETIC" | "C_PUSH" | "C_POP" | "C_LABEL" | "C_GOTO" | "C_IF" | "C_FUNCTION" | "C_RETURN" | "C_CALL"
        rtype: str
        """
        command_type = COMMAND_TYPE_MAP.get(self.current_instruction.split()[0])
        if command_type is None:
            raise ValueError(f"Invalid command: {self.current_instruction}")
        return command_type

    def arg1(self):
        """
        Returns the first argument of the current command. In the case of C_ARITHMETIC, the command itself
        (add, sub, etc.) is returned. Should not be called if the current command is C_RETURN.
        Returns: string
        """
        command_type = self.command_type()
        if command_type == 'C_ARITHMETIC':
            return self.current_command # add, sub, etc.
        elif command_type == 'C_RETURN':
            raise ValueError("C_RETURN command has no arguments")
        else:
            return self.current_command.split()[1] # push, pop, label, goto, if-goto, function, call

    def arg2(self):
        """
        Returns the second argument of the current command. Should be called only if the current command
        is C_PUSH, C_POP, C_FUNCTION, or C_CALL.
        Returns: int
        """
        command_type = self.command_type()
        if command_type in ('C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL'):
            return int(self.current_instruction.split()[2]) # int
        else:
            raise ValueError(f"Invalid command: {self.current_instruction}")
        

