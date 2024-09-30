#!/opt/homebrew/bin/python3 

from unittest import TestCase, main 
import os
import sys  
from unittest.mock import patch, mock_open, MagicMock

# from .. import HackAssembler
from ..HackAssembler.HackAssembler import HackAssembler

class TestHackAssembler(TestCase):
    def setUp(self):
        pass
        
    @patch('os.path', return_value=MagicMock())
    def test_first_pass_add(self, mock_path):
        """
        Test the first pass of the HackAssembler.
        
        Args: 
            mock_file: Mock file object that simulates the file opened by the builtins.open function.
            mock_path: Mock object that simulates the os.path.exists function.    
        """
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

        pass 
    
    #FIXME: This test is not working    
    @patch('os.path', return_value=MagicMock())
    @patch('builtins.open', new_callable=mock_open)
    def test_first_pass_dummy(self, mock_file, mock_path):
        instructions = [
            "@2",
            "D=A",
            "@3",
            "D=D+A",
            "@0",
            "M=D"
        ]
        mock_file.return_value.read.return_value = "\n".join(instructions)
        
        self.hack_assembler = HackAssembler("Add.asm")
        self.hack_assembler.first_pass()
        
        # Add your assertions here

            
    def test_second_pass(self):
        pass

    
    @patch('os.path', return_value=MagicMock())
    @patch('builtins.open', new_callable=mock_open, read_data='mock data')
    def test_hack_assembler_initialization(self, mock_file, mock_path):
        self.hack_assembler = HackAssembler("dummy.asm")
        mock_file.assert_called_once_with("dummy.asm", "r")
        self.assertEqual(self.hack_assembler.parser.instructions, ['mock data'])



    # def test_assemble(self):
        # Create a mock HackAssembler instance
        # mock_assembler = Mock()         
        # # Mock the first_pass and second_pass methods
        # mock_assembler.first_pass = Mock()
        # mock_assembler.second_pass = Mock()
        
        # # Call the assemble method
        # mock_assembler.assemble()
        
        # # Assert that first_pass and second_pass were called
        # mock_assembler.first_pass.assert_called_once()
        # mock_assembler.second_pass.assert_called_once()

        # # Assert that the output file was created
        # self.assertTrue(os.path.exists(mock_assembler.output_file_name)) 

    # def test_decimal_to_binary(self):
    #     self.assertEqual(ha.decimal_to_binary(10), "0000000000001010")
    #     self.assertEqual(HackAssembler.decimal_to_binary(0), "0000000000000000")
    #     self.assertEqual(HackAssembler.decimal_to_binary(15), "0000000000001111")
    #     self.assertEqual(HackAssembler.decimal_to_binary(255), "0000000011111111")

    # def test_assemble_add_file(self):
    #     input_file = "Add.asm"
    #     expected_output_file = "Add.hack"
    #     hack_assembler = ha.HackAssembler(input_file)
    #     hack_assembler.assemble()
        
    #     # Check if add.hack file has the same contents as hack_assembler.output_file
    #     with open(expected_output_file, 'r') as file:
    #         expected_contents = file.read()
    #     with open(hack_assembler.output_file_name, 'r') as file:
    #         actual_contents = file.read()
    #     self.assertEqual(expected_contents, actual_contents)

    # def test_assemble_max_file(self):
    #     input_file = "Max.asm"
    #     expected_output_file = "Max.hack"
    #     hack_assembler = HackAssembler(input_file)
    #     hack_assembler.assemble()
        
    #     # Check if max.hack file has the same contents as hack_assembler.output_file
    #     with open(expected_output_file, 'r') as file:
    #         expected_contents = file.read() 
    #     with open(hack_assembler.output_file_name, 'r') as file:
    #         actual_contents = file.read()
    #     self.assertEqual(expected_contents, actual_contents)

    # def test_assemble_pong_file(self):
    #     input_file = "Pong.asm"
    #     expected_output_file = "Pong.hack"
    #     hack_assembler = HackAssembler(input_file)
    #     hack_assembler.assemble()
        
    #     # Check if pong.hack file has the same contents as hack_assembler.output_file
    #     with open(expected_output_file, 'r') as file:
    #         expected_contents = file.read() 
    #     with open(hack_assembler.output_file_name, 'r') as file:
    #         actual_contents = file.read()   
    #     self.assertEqual(expected_contents, actual_contents)    

    # def test_assemble_rect_file(self):
    #     input_file = "Rect.asm"
    #     expected_output_file = "Rect.hack"
    #     hack_assembler = HackAssembler(input_file)
    #     hack_assembler.assemble()
        
    #     # Check if rect.hack file has the same contents as hack_assembler.output_file
    #     with open(expected_output_file, 'r') as file:
    #         expected_contents = file.read() 
    #     with open(hack_assembler.output_file_name, 'r') as file:
    #         actual_contents = file.read()   
    #     self.assertEqual(expected_contents, actual_contents)

    # def test_get_label_address(self):
    #     pass


if __name__ == '__main__':
    main(argv=[
        "test_HackAssembler.TestHackAssembler.test_hack_assembler_initialization",
        # "test_HackAssembler.TestHackAssembler.test_first_pass",
        # "test_HackAssembler.TestHackAssembler.test_second_pass",
        # "test_HackAssembler.TestHackAssembler.test_assemble",
        # "test_HackAssembler.TestHackAssembler.test_decimal_to_binary",
        # "test_HackAssembler.TestHackAssembler.test_assemble_add_file",
        # "test_HackAssembler.TestHackAssembler.test_assemble_max_file",
        # "test_HackAssembler.TestHackAssembler.test_assemble_pong_file",
        # "test_HackAssembler.TestHackAssembler.test_assemble_rect_file",
        # "test_HackAssembler.TestHackAssembler.test_get_label_address"
        ])
    # only run test_test_first_pass 