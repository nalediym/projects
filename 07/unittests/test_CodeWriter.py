import unittest
from VMTranslator.CodeWriter import CodeWriter

class TestCodeWriter(unittest.TestCase):

    def setUp(self):
        # This method will be called before each test
        self.code_writer = CodeWriter("test_output.asm")

    def tearDown(self):
        # This method will be called after each test
        # Close the file if it's still open
        if hasattr(self.code_writer, 'output_file') and not self.code_writer.output_file.closed:
            self.code_writer.output_file.close()

    def test_write_arithmetic(self):
        pass

    def test_write_push_pop(self):
        pass

    def test_write_label(self):
        pass

    def test_write_goto(self):
        pass

    def test_write_if(self):
        pass

    def test_write_function(self):
        pass

    def test_write_call(self):
        pass

    def test_write_return(self):
        pass

    def test_close(self):
        pass

if __name__ == '__main__':
    unittest.main()