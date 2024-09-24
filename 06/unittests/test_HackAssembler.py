import unittest
import os
from unittest.mock import Mock
from HackAssembler import HackAssembler, Parser, Code, SymbolTable, decimal_to_binary
from util import * 

class TestHackAssembler(unittest.TestCase):
    def setUp(self):
        pass

    def test_first_pass(self):
        instructions = [
            "// This file is part of www.nand2tetris.org",
            "// and the book \"The Elements of Computing Systems\"",
            "// by Nisan and Schocken, MIT Press.",
            "// File name: projects/06/add/Add.asm",
            "",
            "// Computes R0 = 2 + 3  (R0 refers to RAM[0])",
            "",
            "@2",
            "D=A",
            "@3",
            "D=D+A",
            "@0",
            "M=D"
        ]
        expected_instructions = [
            "@2",
            "D=A",
            "@3",
            "D=D+A",
            "@0",
            "M=D"            
        ]
        self.parser.instructions = instructions
        self.parser.first_pass()
        self.assertEqual(self.parser.instructions, expected_instructions)
        self.assertEqual(self.symbol_table.symbol_table, {
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            "R4": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7, 
            "R8": 8,
            "R9": 9,
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,  
            "SCREEN": 16384,
            "KBD": 24576,
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,  
            "LOOP": 10,
            "OUTPUT_FIRST": 11,
            "OUTPUT_D": 12,
            "INFINITE_LOOP": 14
        })  

        # test labels
        instructions = [
            "// This file is part of www.nand2tetris.org",
            "// and the book \"The Elements of Computing Systems\"",
            "// by Nisan and Schocken, MIT Press.",
            "// File name: projects/06/max/Max.asm",
            "",
            "// Computes R2 = max(R0, R1)  (R0,R1,R2 refer to RAM[0],RAM[1],RAM[2])",
            "",
            "   @R0",
            "   D=M              // D = first number",
            "   @R1",
            "   D=D-M            // D = first number - second number",
            "   @OUTPUT_FIRST",
            "   D;JGT            // if D>0 (first is greater) goto output_first",
            "   @R1",
            "   D=M              // D = second number",
            "   @OUTPUT_D",
            "   0;JMP            // goto output_d",
            "(OUTPUT_FIRST)",
            "   @R0",
            "   D=M              // D = first number",
            "(OUTPUT_D)",
            "   @R2",
            "   M=D              // M[2] = D (greatest number)",
            "(INFINITE_LOOP)",
            "   @INFINITE_LOOP",
            "   0;JMP            // infinite loop"
        ]
        expected_instructions = [
            "@0",
            "D=M",
            "@1",
            "D=D-M",
            "@10",
            "D;JGT",
            "@1",
            "D=M",
            "@12",
            "0;JMP",
            "@0",
            "D=M",
            "@2",
            "M=D",
            "@14",
            "0;JMP"
        ]
        self.parser.instructions = instructions
        self.parser.first_pass()
        self.assertEqual(self.parser.instructions, expected_instructions)
        # TODO: verify that these are correct
        self.assertEqual(self.symbol_table.symbol_table["OUTPUT_FIRST"], 10)
        self.assertEqual(self.symbol_table.symbol_table["OUTPUT_D"], 12)
        self.assertEqual(self.symbol_table.symbol_table["INFINITE_LOOP"], 14)

    def test_second_pass(self):
        pass

    def test_assemble(self):
        # Create a mock HackAssembler instance
        mock_assembler = Mock(spec=HackAssembler) 
        self.assertTrue(isinstance(mock_assembler, HackAssembler))
        
        # Mock the first_pass and second_pass methods
        mock_assembler.first_pass = Mock()
        mock_assembler.second_pass = Mock()
        
        # Call the assemble method
        mock_assembler.assemble()
        
        # Assert that first_pass and second_pass were called
        mock_assembler.first_pass.assert_called_once()
        mock_assembler.second_pass.assert_called_once()

        # Assert that the output file was created
        self.assertTrue(os.path.exists(mock_assembler.output_file_name)) 

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(10), "0000000000001010")
        self.assertEqual(decimal_to_binary(0), "0000000000000000")
        self.assertEqual(decimal_to_binary(15), "0000000000001111")
        self.assertEqual(decimal_to_binary(255), "0000000011111111")

    def test_assemble_add_file(self):
        input_file = "Add.asm"
        expected_output_file = "Add.hack"
        hack_assembler = HackAssembler(input_file)
        hack_assembler.assemble()
        
        # Check if add.hack file has the same contents as hack_assembler.output_file
        with open(expected_output_file, 'r') as file:
            expected_contents = file.read()
        with open(hack_assembler.output_file_name, 'r') as file:
            actual_contents = file.read()
        self.assertEqual(expected_contents, actual_contents)

    def test_assemble_max_file(self):
        input_file = "Max.asm"
        expected_output_file = "Max.hack"
        hack_assembler = HackAssembler(input_file)
        hack_assembler.assemble()
        
        # Check if max.hack file has the same contents as hack_assembler.output_file
        with open(expected_output_file, 'r') as file:
            expected_contents = file.read() 
        with open(hack_assembler.output_file_name, 'r') as file:
            actual_contents = file.read()
        self.assertEqual(expected_contents, actual_contents)

    def test_assemble_pong_file(self):
        input_file = "Pong.asm"
        expected_output_file = "Pong.hack"
        hack_assembler = HackAssembler(input_file)
        hack_assembler.assemble()
        
        # Check if pong.hack file has the same contents as hack_assembler.output_file
        with open(expected_output_file, 'r') as file:
            expected_contents = file.read() 
        with open(hack_assembler.output_file_name, 'r') as file:
            actual_contents = file.read()   
        self.assertEqual(expected_contents, actual_contents)    

    def test_assemble_rect_file(self):
        input_file = "Rect.asm"
        expected_output_file = "Rect.hack"
        hack_assembler = HackAssembler(input_file)
        hack_assembler.assemble()
        
        # Check if rect.hack file has the same contents as hack_assembler.output_file
        with open(expected_output_file, 'r') as file:
            expected_contents = file.read() 
        with open(hack_assembler.output_file_name, 'r') as file:
            actual_contents = file.read()   
        self.assertEqual(expected_contents, actual_contents)

    def test_get_label_address(self):
        pass


if __name__ == '__main__':
    unittest.main()