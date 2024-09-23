import unittest
import unittest.mock as mock
from vm_translator import VMTranslator
import os
import sys
from unittest.mock import patch, mock_open, MagicMock

class TestVMTranslator(unittest.TestCase):
    def setUp(self):
        self.test_dir = "07/MemoryAccess/BasicTest"
        self.vm_file = os.path.join(self.test_dir, "BasicTest.vm")
        self.translator = VMTranslator(self.vm_file)

    def test_translate(self):
        input_content = "push constant 17"
        expected_output = """
            @17
            D=A
            @SP
            A=M
            M=D
            @SP
            M=M+1
        """
        
        mock_input = mock_open(read_data=input_content)
        mock_output = mock_open()
        
        with patch('builtins.open', mock_input), \
             patch('builtins.open', mock_output):
            VMTranslator("test.vm").translate()
        
        mock_output().write.assert_called_once_with(expected_output)

    def test_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            VMTranslator("non_existent_file.vm")

    def test_main(self):        
        @patch('sys.argv', ['vm_translator.py', 'test.vm'])
        def test_main_with_vm_file(self):
            with self.assertRaises(SystemExit) as cm:
                from vm_translator import VMTranslator
                VMTranslator.main()
            self.assertEqual(cm.exception.code, 0)
            self.assertTrue(any(arg.endswith('.vm') for arg in sys.argv[1:]))

        @patch('sys.argv', ['vm_translator.py'])
        def test_main_without_vm_file(self):
            with self.assertRaises(SystemExit) as cm:
                from vm_translator import VMTranslator
                VMTranslator.main()
            self.assertEqual(cm.exception.code, 1)
            self.assertFalse(any(arg.endswith('.vm') for arg in sys.argv[1:]))

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()