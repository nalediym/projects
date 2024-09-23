import unittest
from HackAssembler.SymbolTable import SymbolTable

class TestSymbolTable(unittest.TestCase):
    def setUp(self):
        self.symbol_table = SymbolTable()

    def test_add_entry(self):
        self.symbol_table.addEntry("LOOP", 16)
        self.assertTrue(self.symbol_table.contains("LOOP"))
        self.assertEqual(self.symbol_table.getAddress("LOOP"), 16)

    def test_add_entry_invalid_symbol(self):
        with self.assertRaises(ValueError):
            self.symbol_table.addEntry("@LOOP", 16)
        with self.assertRaises(ValueError):
            self.symbol_table.addEntry("(LOOP)", 16)

    def test_contains(self):
        self.assertTrue(self.symbol_table.contains("SP"))
        self.assertTrue(self.symbol_table.contains("R15"))
        self.assertFalse(self.symbol_table.contains("UNKNOWN"))

    def test_getAddress(self):
        self.assertEqual(self.symbol_table.getAddress("SP"), 0)
        self.assertEqual(self.symbol_table.getAddress("LCL"), 1)
        self.assertEqual(self.symbol_table.getAddress("R15"), 15)

    def test_getAddress_invalid_symbol(self):
        with self.assertRaises(ValueError):
            self.symbol_table.getAddress("@SP")

    def test_getAddress_unknown_symbol(self):
        with self.assertRaises(ValueError):
            self.symbol_table.getAddress("UNKNOWN")

    def test_validate_symbol(self):
        self.assertTrue(self.symbol_table.validate_symbol("LOOP"))
        self.assertTrue(self.symbol_table.validate_symbol("R16"))
        self.assertFalse(self.symbol_table.validate_symbol("@LOOP"))
        self.assertFalse(self.symbol_table.validate_symbol("(LOOP)"))
        self.assertFalse(self.symbol_table.validate_symbol("LOOP)"))

    def test_predefined_symbols(self):
        predefined_symbols = ["SP", "LCL", "ARG", "THIS", "THAT"] + [f"R{i}" for i in range(16)]
        for symbol in predefined_symbols:
            self.assertTrue(self.symbol_table.contains(symbol))

if __name__ == '__main__':
    unittest.main()