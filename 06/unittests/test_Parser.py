#!/bin/env python3 

import unittest
from ..HackAssembler.Parser import Parser, A_INSTRUCTION, C_INSTRUCTION, L_INSTRUCTION

class TestParser(unittest.TestCase):
    def setUp(self):
        """
        Set up the parser with a test file
        """
        self.parser = Parser("test_input.asm")

    def test_hasMoreLines(self):
        
        # Test that the empty file returns False

        # Test that the file with one line returns True

        # Test that the file with two lines returns True
        pass


    def test_advance(self):
        pass

    def test_instructionType(self):
        # Test A-instruction
        self.parser.current_instruction = "@100"
        self.assertEqual(self.parser.instructionType(), A_INSTRUCTION)

        self.parser.current_instruction = "@R0"
        self.assertEqual(self.parser.instructionType(), A_INSTRUCTION)

        # Test L-instruction
        self.parser.current_instruction = "(LOOP)"
        self.assertEqual(self.parser.instructionType(), L_INSTRUCTION)

        # Test C-instruction
        self.parser.current_instruction = "D=M"
        self.assertEqual(self.parser.instructionType(), C_INSTRUCTION)

        self.parser.current_instruction = "M=D+A"
        self.assertEqual(self.parser.instructionType(), C_INSTRUCTION)

        self.parser.current_instruction = "0;JMP"
        self.assertEqual(self.parser.instructionType(), C_INSTRUCTION)

        # Test invalid instruction
        self.parser.current_instruction = "INVALID"
        with self.assertRaises(ValueError):
            self.parser.instructionType()

    def test_symbol(self):
        pass

    def test_dest(self):
        pass

