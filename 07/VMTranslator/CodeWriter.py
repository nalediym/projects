import os
from dataclasses import dataclass
from types import MethodType


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
    
    def _write_push(self, segment: str, index: int) -> str:
        """
        Write the assembly code for a push command.

        Args:
            segment (str): The segment to push to.
            index (int): The index to push.

        Returns:
            str: The assembly code for the push command.    
        """
        assembly_code = ""
        
        segment_pointer_address: str = self._get_segment_pointer_address(segment, index)

        assembly_code_push_address = f"""
                @addr
                D=M 
                @SP 
                A=M
                M=D // RAM[SP] = D
                @SP
                M=M+1 // SP++
            """
        
        assembly_code = segment_pointer_address + assembly_code_push_address
        return assembly_code 

    def _get_segment_pointer_address(self, segment: str, index: int) -> str:
        """
        Get the address of the segment.
        Args:
            segment (str): The segment to get the pointer address for.
            index (int): The index of the pointer.
        Returns:
            str: Asm code to set/get the segment pointer address.
        """

        assembly_code = ""

        if segment == 'local': 
            assembly_code = f"""
                @{index}
                D=A
                @LCL
                A=M+D
                D=M // RAM[LCL + index]
                @addr
                M=D // RAM[addr] = RAM[LCL + index]
            """
        elif segment == 'argument':
            assembly_code = f"""
                @{index}
                D=A
                @ARG
                A=M+D
                D=M // RAM[ARG + index]
                @addr
                M=D // RAM[addr] = RAM[ARG + index]
            """
        elif segment == 'this':
            assembly_code = f"""
                @{index}
                D=A
                @THIS
                A=M+D
                D=M // RAM[THIS + index]
                @addr
                M=D // RAM[addr] = RAM[THIS + index]
            """
        elif segment == 'that':
            assembly_code = f"""
                @{index}
                D=A
                @THAT
                A=M+D
                D=M // RAM[THAT + index]
                @addr
                M=D // RAM[addr] = RAM[THAT + index]
            """
        elif segment == 'constant':
            assembly_code = f"""
                @{index}
                D=A
                @addr
                M=D // RAM[addr] = index
            """
        elif segment == 'static':
            static_segement_addr_symbol = f"{self.output_file_name}.{index}"
            assembly_code = f"""
                @{index}
                D=A
                @{static_segement_addr_symbol}
                M=D // RAM[STATIC] = index
                @addr
                M=D // RAM[addr] = RAM[{static_segement_addr_symbol}]
            """
        elif segment == 'temp':
            assembly_code = f"""
                @{index}
                D=A
                @5
                A=A+D
                D=M // RAM[5 + index]
                @addr
                M=D // RAM[addr] = RAM[5 + index]
            """
        elif segment == 'pointer':
            if index == 0:
                assembly_code = f"""
                    @THIS
                    D=M
                    @addr
                    M=D // RAM[addr] = RAM[THIS]
                """
            elif index == 1:
                assembly_code = f"""
                    @THAT
                    D=M
                    @addr
                    M=D // RAM[addr] = RAM[THAT]
                """
            else:
                raise ValueError(f"Invalid index: {index}. Must be 0 or 1")
        else:
            raise ValueError(f"Invalid segment: {segment}")

        return assembly_code
            

    def _write_pop(self, segment: str, index: int) -> str:
        """
        Write the assembly code for a pop command.

        Args:
            segment (str): The segment to pop from.
            index (int): The index to pop.

        Returns:
            str: The assembly code for the pop command.     
        """
        assembly_code = ""
        segment_pointer_address: str = self._get_segment_pointer_address(segment, index)

        assembly_code_pop_address = f"""
                // SP--
                @SP
                M=M-1
                D=M // D = RAM[SP]
                // RAM[addr] = RAM[SP]
                @addr
                M=D // RAM[addr] = RAM[SP]
            """
        assembly_code = \
            segment_pointer_address \
            + assembly_code_pop_address
        return assembly_code

    def writeArithmetic(self, command: str) -> str:
        """
        Writes to the output file the assembly code that implements the given arithmetic-logical command.
        Args:
            command (str): The arithmetic command. Must be one of: add, sub, neg, eq, gt, lt, and, or, not.
        Returns:
            str: The assembly code for the given arithmetic command.
        """
        # Implement the logic to write assembly code for arithmetic operations
        assembly_code = ""
        arithmetic_variables_assembly_code = self._get_arithmetic_variables_from_stack(command)
        if command == 'add':
            arithmatic_assembly_code = self._add()
        elif command == 'sub':
            arithmatic_assembly_code = self._sub()
        elif command == 'neg':
            arithmatic_assembly_code = self._neg()
        elif command == 'eq':
            arithmatic_assembly_code = self._eq()
        elif command == 'gt':
            arithmatic_assembly_code = self._gt()
        elif command == 'lt':
            arithmatic_assembly_code = self._lt()
        elif command == 'and':
            arithmatic_assembly_code = self._and()
        elif command == 'or':
            arithmatic_assembly_code = self._or()
        elif command == 'not':
            arithmatic_assembly_code = self._not()
        else:
            raise ValueError(f"Invalid command: {command}. Must be add, sub, neg, eq, gt, lt, and, or, not")
        
        push_result_assembly_code = self._push_result_to_stack()
        assembly_code = arithmetic_variables_assembly_code + arithmatic_assembly_code + push_result_assembly_code
        return assembly_code
    
    def _push_result_to_stack(self) -> str:
        return f"""
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        """
    def _get_arithmetic_variables_from_stack(self, arithmetic_command: str) -> str:
        """
        Define the variables for the arithmetic command.
        Returns:
            str: The assembly code for the given command.
        """
        assembly_code = ""
        if arithmetic_command == 'add':
            assembly_code = self._get_x_from_stack() + self._get_y_from_stack()
        elif arithmetic_command == 'sub':
            assembly_code = self._get_x_from_stack() + self._get_y_from_stack()
        elif arithmetic_command == 'neg':
            assembly_code = self._get_y_from_stack()
        elif arithmetic_command == 'eq':
            assembly_code = self._get_x_from_stack() + self._get_y_from_stack()
        elif arithmetic_command == 'gt':
            assembly_code = self._get_x_from_stack() + self._get_y_from_stack()
        elif arithmetic_command == 'lt':
            assembly_code = self._get_x_from_stack() + self._get_y_from_stack()
        elif arithmetic_command == 'and':
            assembly_code = self._get_x_from_stack() + self._get_y_from_stack()
        elif arithmetic_command == 'or':
            assembly_code = self._get_x_from_stack() + self._get_y_from_stack()
        elif arithmetic_command == 'not':
            assembly_code = self._get_x_from_stack()
        else:
            raise ValueError(f"Invalid arithmetic command: {arithmetic_command}. Must be add, sub, neg, eq, gt, lt, and, or, not")
        return assembly_code

    def _get_x_from_stack(self) -> str:
        return f"""
                // get x from stack
                @SP
                M=M-1
                A=M
                D=M
                @x
                M=D
        """
    
    def _get_y_from_stack(self) -> str:
        return f"""
                // get y from stack
                @SP
                M=M-1
                A=M
                D=M
                @y
                M=D
        """
    
    def _add(self) -> str:
        """
        Add two values.
        Args:
            x (int): The first value.
            y (int): The second value.
        Returns:
            str: The assembly code for the given command.
        """
        return f"""
                @x
                D=M
                @y
                D=D+M
                @result
                M=D
        """
    
    def _sub(self) -> str:
        """
        Subtract two values.
        """
        return f"""
                @x
                D=M
                @y
                D=D-M
                @result
                M=D
        """
    
    def _neg(self) -> str:
        """
        Negate a value.
        Args:
            y (int): The value to negate.
        Returns:
            str: The assembly code for the given command.
        """
        return f"""
                @y
                D=M
                @result
                M=-D
        """
    
    def _eq(self) -> str:
        """
        Compare two values to see if they are equal.
        Returns:
            str: The assembly code for the given command.
        """
        return f"""
                @x
                D=M
                @y
                D=D-M
                @true
                D;JEQ // if x == y
                @false
                D;JNE // if x != y
                (true)
                @result
                M=1
                (false)
                @result
                M=0
        """
    def _gt(self) -> str:
        """
        Compare two values to see if the first is greater than the second.
        Returns:
            str: The assembly code for the given command.
        """
        return f"""
                @x
                D=M 
                @y
                D=D-M
                @true
                D;JGT // if x > y 
                @false
                D;JLE // if x <= y
                (true)
                @result
                M=1
                (false)
                @result
                M=0
        """
    
    def _lt(self) -> str:
        """
        Compare two values.
        Returns:
            str: The assembly code for the given command.
        """
        return f"""
                @x
                D=M
                @y
                D=D-M
                @true
                D;JLT // if x < y
                @false
                D;JGE // if x >= y
                (true)
                @result
                M=1
                (false)
                @result
                M=0
        """
    
    def _and(self) -> str:
        """
        AND two values.
        Returns:
            str: The assembly code for the given command.
        """
        return f"""
                @x
                D=M
                @y
                D=D&M
                @true
                D;JGE // if x & y >= 1 // if 1 & 1  
                @false
                D;JLT // if x & y == 0 // if 0 & 0
                (true)
                @result
                M=1
                (false)
                @result
                M=0
        """
    
    def _or(self) -> str:
        """
        OR two values.
        Returns:
            str: The assembly code for the given command.
        """
        return f"""
                @x
                D=M 
                @y
                D=D|M
                @true
                D;JGE // if x | y >= 1 // if 1 | 1
                @false
                D;JLT // if x | y == 0 // if 0 | 0
                (true)
                @result
                M=1
                (false)
                @result
                M=0
        """
    
    def _not(self) -> str:
        """
        NOT a value.
        Returns:
            str: The assembly code for the given command.
        """
        return f"""
                @x
                D=M 
                @true
                D;JEQ // if x == 0
                @false
                D;JNE // if x != 0
                (true)
                @result
                M=1
                (false)
                @result
                M=0
        """
    

    def _gt(self) -> str:
        """
        Compare two values.
        Returns:
            str: The assembly code for the given command.
        """
        return f"""
                @x
                D=M
                @y
                D=D-M
                @true
                D;JGT // if x > y
                @false
                D;JLE // if x <= y
                (true)
                @result
                M=1
                (false)
                @result
                M=0
        """

    def writePushPop(self, command: str, segment: str, index: int) -> str:
        """
        Writes to the output file the assembly code that implements the given push or pop command.
        Args:
            command (str): Either C_PUSH or C_POP.
            segment (str): The memory segment to operate on ( e.g. local, argument, this, that, constant, static, pointer, or temp)
            index (int): The index in the memory segment.
        Returns:
            str: The assembly code for the given push/pop command.
        """
        # Implement the logic to write assembly code for push/pop operations
        if command == 'C_PUSH':
            assembly_code = self._write_push(segment, index)
        elif command == 'C_POP':
            assembly_code = self._write_pop(segment, index)
        else:
            raise ValueError(f"Invalid command: {command}. Must be C_PUSH or C_POP")
        return assembly_code
    
    def close(self):
        """
        Closes the output file.
        """
        if self.output:
            self.output.close()

