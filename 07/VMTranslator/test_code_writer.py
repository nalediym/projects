import unittest
from code_writer import CodeWriter
from unittest import mock

class TestCodeWriter(unittest.TestCase):
    def setUp(self):
        self.code_writer = CodeWriter("test_output.asm")

    def tearDown(self):
        self.code_writer.close()

    def test_close(self):
        mock_file = mock.Mock()
        self.code_writer.output = mock_file
        self.code_writer.close()
        mock_file.close.assert_called_once()

    def test_push_temp(self):
        symbol = "temp"
        i = 3
        given_vm_command = "push temp 3"
        expected_output = "push RAM[8]"
        out = self.code_writer.push_temp(symbol, i)
        self.assertEqual(out, expected_output)

    def test_pop_temp(self):

        symbol = "temp"
        i = 3
        given_vm_command = "pop temp 3"
        expected_output = "pop RAM[8]"
        out = self.code_writer.pop_temp(symbol, i)
        self.assertEqual(out, expected_output)

    def test_push_pointer(self):
        symbol = "pointer"
        i = 0
        given_vm_command = "push pointer 0"
        expected_output = "push THIS"
        out = self.code_writer.push_pointer(symbol, i)
        self.assertEqual(out, expected_output)

        given_vm_command = "push pointer 1"
        expected_output = "push THAT"
        out = self.code_writer.push_pointer(symbol, i)
        self.assertEqual(out, expected_output)

    def test_pop_pointer(self):
        symbol = "pointer"
        i = 0
        given_vm_command = "pop pointer 0"
        expected_output = "pop THIS"

    def test_write_arithmetic(self):
        self.code_writer.write_arithmetic("add")
        # Add assertions here to check the output

    def test_write_push_pop(self):
        self.code_writer.write_push_pop("C_PUSH", "local", 0)
        # Add assertions here to check the output

    def test_push_pointer(self):
        symbol = "pointer"
        i = 0
        given_vm_command = "push pointer 0"
        expected_output = "push THIS"
        out = self.code_writer.push_pointer(symbol, i)
        self.assertEqual(out, expected_output)

    

    

    
if __name__ == '__main__':
    unittest.main()