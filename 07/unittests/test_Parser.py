import unittest
from unittest.mock import patch, mock_open

# Add the parent directory to the Python path to import the Parser
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from VMTranslator.Parser import Parser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.test_vm_content = """
        // This is a comment
        push constant 7
        pop local 0
        add
        label LOOP_START
        goto LOOP_START
        function SimpleFunction.test 2
        return
        """

    @patch('os.path.exists')
    def test_parser_initialization(self, mock_exists):
        mock_exists.return_value = True 
        with patch('builtins.open', mock_open(read_data=self.test_vm_content)):
            parser = Parser('test.vm')
            self.assertEqual(parser.input_file, 'test.vm')
            self.assertEqual(parser.current_line_number, 0)
            self.assertEqual(parser.current_instruction, 'push constant 7')

        with self.assertRaises(ValueError):
            Parser('invalid.txt')
        
        mock_exists.return_value = False
        with self.assertRaises(FileNotFoundError):
            Parser('nonexistent.vm')

    @patch('os.path.exists', return_value=True)
    def test_has_more_lines(self, mock_exists):
        with patch('builtins.open', mock_open(read_data=self.test_vm_content)):
            parser = Parser('test.vm')
            self.assertTrue(parser.has_more_lines())
            
            # Advance to the last line
            while parser.has_more_lines():
                parser.advance()
            self.assertFalse(parser.has_more_lines())

    @patch('os.path.exists', return_value=True)
    def test_advance(self, mock_exists):
        with patch('builtins.open', mock_open(read_data=self.test_vm_content)):
            parser = Parser('test.vm')
            self.assertEqual(parser.current_instruction, 'push constant 7')
            parser.advance()
            self.assertEqual(parser.current_instruction, 'pop local 0')

    @patch('os.path.exists', return_value=True)
    def test_command_type(self, mock_exists):
        with patch('builtins.open', mock_open(read_data=self.test_vm_content)):
            parser = Parser('test.vm')
            self.assertEqual(parser.commandType(), 'C_PUSH')
            parser.advance()
            self.assertEqual(parser.commandType(), 'C_POP')
            parser.advance()
            self.assertEqual(parser.commandType(), 'C_ARITHMETIC')

    @patch('os.path.exists', return_value=True)
    def test_arg1(self, mock_exists):
        with patch('builtins.open', mock_open(read_data=self.test_vm_content)):
            parser = Parser('test.vm')
             # push constant 7
            self.assertEqual(parser.arg1(), 'constant')
            parser.advance()  # pop local 0
            self.assertEqual(parser.arg1(), 'local')
            parser.advance()  # add
            self.assertEqual(parser.arg1(), 'add')

    @patch('os.path.exists', return_value=True)
    def test_arg2(self, mock_exists):
        with patch('builtins.open', mock_open(read_data=self.test_vm_content)):
            parser = Parser('test.vm')
            # push constant 7
            self.assertEqual(parser.arg2(), 7)
            parser.advance()  # pop local 0
            self.assertEqual(parser.arg2(), 0)
            
            # Test arg2 for non-applicable command
            parser.advance()  # add
            with self.assertRaises(ValueError):
                parser.arg2()

if __name__ == '__main__':
    unittest.main()