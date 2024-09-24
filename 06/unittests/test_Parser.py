#!/bin/env python3 

import unittest
from ..HackAssembler.Parser import Parser, A_INSTRUCTION, C_INSTRUCTION, L_INSTRUCTION

class TestParser(unittest.TestCase):
    def setUp(self):
        """
        Set up the parser with a test file
        """
        self.parser = Parser("test_input.asm")
    
    def test_init(self):
        self.assertEqual(self.parser.input_file, "test_input.asm")
        self.assertEqual(self.parser.current_instruction, None)
        self.assertEqual(self.parser.current_line_number, 0)
        self.assertEqual(self.parser.instructions, [])
        self.assertEqual(self.parser.current_instruction_index, 0)

        # test when the file does not exist
        with self.assertRaises(FileNotFoundError):
            Parser("nonexistent.asm")
        

    def test_hasMoreLines(self):
        # Test that the empty file returns False
        self.parser.current_instruction_index = 0
        self.parser.instructions = []
        self.assertFalse(self.parser.hasMoreLines())

        # Test that the file with one line returns True
        self.parser.instructions = ["@R0"]
        self.assertTrue(self.parser.hasMoreLines())

        # Test that the file with two lines and the second is a comment returns True
        self.parser.current_instruction_index = 1
        self.parser.instructions = ["@R0", "(LOOP)"]
        self.parser.advance()
        self.assertTrue(self.parser.hasMoreLines())
        self.parser.advance()
        self.assertFalse(self.parser.hasMoreLines())


    def test_advance(self):
        # Test that the file with two lines returns True
        self.parser.instructions = ["@R0", "(LOOP)"]
        self.parser.advance()
        # Test that the current instruction is set to the first instruction
        self.assertEqual(self.parser.current_instruction, "@R0")
        self.assertEqual(self.parser.current_line_number, 0)
        self.parser.advance()
        self.assertEqual(self.parser.current_instruction, "(LOOP)")
        self.assertEqual(self.parser.current_line_number, 1)

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
        # Test A-instruction
        self.parser.current_instruction = "@sum"
        self.assertEqual(self.parser.symbol(), "sum")

        self.parser.current_instruction = "@100"
        self.assertEqual(self.parser.symbol(), "100")

        self.parser.current_instruction = "@R0"
        self.assertEqual(self.parser.symbol(), "R0")

        # Test L-instruction
        self.parser.current_instruction = "(LOOP)"
        self.assertEqual(self.parser.symbol(), "LOOP")

    def test_dest(self):
        self.parser.current_instruction = "D=D+1;JLE"
        self.assertEqual(self.parser.dest(), "D")

        self.parser.current_instruction = "M=-1"
        self.assertEqual(self.parser.dest(), "M")

        self.parser.current_instruction = "0;JMP"
        self.assertEqual(self.parser.dest(), "null")

    def test_comp(self):
        self.parser.current_instruction = "D=D+1;JLE"
        self.assertEqual(self.parser.comp(), "D+1")

        self.parser.current_instruction = "M=-1"
        self.assertEqual(self.parser.comp(), "-1")

        self.parser.current_instruction = "0;JMP"
        self.assertEqual(self.parser.comp(), "0")


    def test_jump(self):
        self.parser.current_instruction = "D=D+1;JLE"
        self.assertEqual(self.parser.jump(), "JLE")

        self.parser.current_instruction = "M=-1"
        self.assertEqual(self.parser.jump(), "null")

        self.parser.current_instruction = "0;JMP"
        self.assertEqual(self.parser.jump(), "JMP")

    def test_contains_dest_field(self):
        self.parser.current_instruction = "D=D+1;JLE"
        self.assertTrue(self.parser._contains_dest_field())

        self.parser.current_instruction = "M=-1"
        self.assertTrue(self.parser._contains_dest_field())

        self.parser.current_instruction = "0;JMP"
        self.assertFalse(self.parser._contains_dest_field())

    def test_contains_jump_field(self):
        self.parser.current_instruction = "D=D+1;JLE"
        self.assertTrue(self.parser._contains_jump_field())

        self.parser.current_instruction = "M=-1"
        self.assertFalse(self.parser._contains_jump_field())

        self.parser.current_instruction = "0;JMP"
        self.assertTrue(self.parser._contains_jump_field())


