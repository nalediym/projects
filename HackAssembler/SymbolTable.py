class SymbolTable:
    def __init__(self):
        # Initialize the symbol table with predefined symbols
        self.table = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'R0': 0,
            'R1': 1,
            # ... add more predefined symbols ...
            'SCREEN': 16384,
            'KBD': 24576
        }

    def add_entry(self, symbol, address):
        # Add a new entry to the symbol table
        self.table[symbol] = address

    def contains(self, symbol):
        # Check if the symbol table contains the given symbol
        return symbol in self.table

    def get_address(self, symbol):
        # Get the address associated with the symbol
        return self.table.get(symbol)