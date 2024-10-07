import unittest
import os
import subprocess

class TestSimpleAdd(unittest.TestCase):
    def setUp(self):
        # Compile the VM code to hack assembly
        os.system('python ../../VMTranslator.py SimpleAdd.vm')
        
        # Use the CPUEmulator to run the assembly code
        result = subprocess.run(['../../tools/CPUEmulator.sh', 'SimpleAdd.tst'], 
                                capture_output=True, text=True)
        self.output = result.stdout

    def test_simple_add(self):
        # Check if the output contains the expected result
        self.assertIn('|   256   |     15  |', self.output)

    def tearDown(self):
        # Clean up generated files
        os.remove('SimpleAdd.asm')
        os.remove('SimpleAdd.out')

if __name__ == '__main__':
    unittest.main()
