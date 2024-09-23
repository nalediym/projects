import unittest
import os
from unittest.mock import Mock
from HackAssembler import HackAssembler
from util import * 

class TestHackAssembler(unittest.TestCase):
    def setUp(self):
        pass

    def test_first_pass(self):
        pass

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


if __name__ == '__main__':
    unittest.main()