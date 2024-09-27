import re

REGEX_FOR_C_INSTRUCTION = "{dest} = {comp} ; {jump} "

VALID_DEST_FIELDS = ["null", "M", "D", "MD", "A", "AM", "AD", "AMD"]
VALID_COMP_FIELDS = ["0", "1", "-1", "D", "A", "!D", "!A", "-D", "-A", "D+1", "A+1", "D-1", "A-1", "D+A", "D-A", "A-D", "D&A", "D|A", "M", "!M", "-M", "M+1", "M-1", "D+M", "D-M", "M-D", "D&M", "D|M"]
VALID_JUMP_FIELDS = ["null", "JGT", "JEQ", "JGE", "JLT", "JNE", "JLE", "JMP"]

class Code:
    """
    Deals only with C-instructions:  dest = comp ; jump    
    """

    def __init__(self):
        pass # do nothing per instructions

    def _validate_comp_field(self, comp_field: str) -> bool:
        """
        Validates the comp field of a C-INSTRUCTION.

        Args:
            comp_field (str): The current comp field of a C-INSTRUCTION. (eg. "D&M")

        Returns:
            bool: True if the comp field is valid, False otherwise.
        """
        return comp_field in VALID_COMP_FIELDS
    
    def _validate_dest_field(self, dest_field: str) -> bool:
        """
        Validates the dest field of a C-INSTRUCTION.

        Args:
            dest_field (str): The current dest field of a C-INSTRUCTION. (eg. "D")

        Returns:
            bool: True if the dest field is valid, False otherwise.
        """
        return dest_field in VALID_DEST_FIELDS

    def _validate_jump_field(self, jump_field: str) -> bool:
        """
        Validates the jump field of a C-INSTRUCTION.

        Args:
            jump_field (str): The current jump field of a C-INSTRUCTION. (eg. "JNE")

        Returns:
            bool: True if the jump field is valid, False otherwise. 
        """
        return jump_field in VALID_JUMP_FIELDS

    def comp(self, comp_bits: str) -> str:
        """
        Returns the binary representation of the parsed comp field (string)
        
        Returns the a bit and the 6 c bits of the current comp from a C-INSTRUCTION.

        Args:
            comp_bits (str): The current C-INSTRUCTION. (eg. "D&M")

        Returns:    
            str: The a bit and the 6 c bits of the current C-INSTRUCTION. (eg. "1000000")
        """
        if not self._validate_comp_field(comp_bits):
            raise ValueError(f"Invalid comp field: {comp_bits}")
        # TODO: Add M+A to the c_bits_map. Verify if this is the best way to handle this.
        c_bits_map = {
            "0": "101010", 
            "1": "111111",
            "-1": "111010",
            "D": "001100",
            "A": "110000",
            "M": "110000", 
            "!D": "001101",
            "!A": "011001",
            "!M": "011001",
            "-D": "001111",
            "-A": "011011",
            "-M": "011011",
            "D+1": "001111",
            "A+1": "011011",
            "M+1": "011011",
            "D-1": "001110",
            "A-1": "011001",
            "M-1": "011001",
            "D+A": "000010",
            "D+M": "000010",
            "D-A": "010011",
            "D-M": "010011",
            "A-D": "000111",
            "M-D": "000111",   
            "D&A": "000000",
            "D&M": "000000",
            "D|A": "010101",
            "D|M": "010101"
        } 
        A_BIT_ZERO = ["0", 
                      "1", 
                      "-1",
                      "D",
                      "A",
                      "M",
                      "!D",
                      "!A",
                      "!M",
                      "-D",
                      "-A",
                      "D+1",
                      "A+1",
                      "M+1",
                      "D-1",
                      "A-1",
                      "M-1",
                      "D+A",
                      "D-A",
                      "A-D",
                      "D&A",
                      "D|A"
                      ]
        A_BIT_ONE = ["M",
                     "!M",
                     "-M",
                     "M+1",
                     "M-1",
                     "D+M",
                     "D-M",
                     "M-D",
                     "D&M",
                     "D|M"
                     ]
        a_bit_map = {
            **{ k: "0" for k in A_BIT_ZERO}, 
            **{ k: "1" for k in A_BIT_ONE}
        }
        comp_instruction = a_bit_map[comp_bits] + c_bits_map[comp_bits]
        return comp_instruction

    def jump(self, jump_bits: str) -> str:
        """
        Returns the binary representation of the parsed jump field (string)

        Args:
            instruction (str): The current C-INSTRUCTION. (eg. "JNE")

        Returns:
            str: The j bits of the current C-INSTRUCTION. (eg. "101")
        """
        if not self._validate_jump_field(jump_bits):
            raise ValueError(f"Invalid jump field: {jump_bits}")
        jump_map = {
            "null": "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111"
        }   
        return jump_map.get(jump_bits)
    
    def _validate_dest_field(self, dest_bits: str) -> bool:
        """
        Validates the dest field of a C-INSTRUCTION.

        Args:
            dest_bits (str): The current dest field of a C-INSTRUCTION. (eg. "D")

        Returns:
            bool: True if the dest field is valid, False otherwise.
        """ 
        return dest_bits in VALID_DEST_FIELDS

    def dest(self, dest_bits: str) -> str:
        """
        Returns the binary representation of the parsed dest field (string)

        Args:
            instruction (str): The current C-INSTRUCTION. (eg. "D")

        Returns:
            str: The d bits of the current C-INSTRUCTION. (eg. "010")
        """
        if not self._validate_dest_field(dest_bits):
            raise ValueError(f"Invalid dest field: {dest_bits}")
        dest_map = {
            "null": "000",
            "M": "001",
            "D": "010",
            "DM": "011",
            "A": "100",
            "AM": "101",
            "AD": "110",
            "AMD": "111"
        }
        return dest_map.get(dest_bits)