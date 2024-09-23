import re

REGEX_FOR_C_INSTRUCTION = "{dest} = {comp} ; {jump} "

class Code:
    """
    Deals only with C-instructions:  dest = comp ; jump    
    """
    def __init__(self, instruction: str):
        """

        """
        self.instruction = instruction # e.g: ""
        self._validate_instruction(instruction)

    def _validate_instruction(self, instruction: str):
        """
        Check if instruction is a valid 16 bit C-instruction and raise error if not
        Input:
            instruction (str): The current C-INSTRUCTION. (eg: "A = A+1")
        """
        pass


    def comp(self, instruction: str):
        """
        Returns the binary representation of the parsed comp field (string)
        
        Returns the c bits of the current C-INSTRUCTION.

        Args:
            instruction (str): The current C-INSTRUCTION. (eg. "A+1")

        Returns:    
            str: The c bits of the current C-INSTRUCTION. (eg. "0110111")
        """
        pass

    def jump(self, instruction: str):
        """
        Returns the binary representation of the parsed jump field (string)

        Args:
            instruction (str): The current C-INSTRUCTION. (eg. "JNE")

        Returns:
            str: The j bits of the current C-INSTRUCTION. (eg. "101")
        """
        pass

    def dest(self, instruction: str):
        """
        Returns the binary representation of the parsed dest field (string)

        Args:
            instruction (str): The current C-INSTRUCTION. (eg. "D")

        Returns:
            str: The d bits of the current C-INSTRUCTION. (eg. "001")
        """
        pass
