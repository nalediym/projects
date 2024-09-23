class SymbolTable:
    """
    handles symbols
    """
    def __init__(self):
        """
        Creates and initializes a SymbolTable
        Creates a new empty symbol table
        """
        self.symbol_table = {
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            **{f"R{i}": i for i in range(16)}, # TODO: replace 16 with the total number of registers 
        }

    def addEntry(self, symbol: str, address: int) -> None:
        """
        Adds <symbol, address> to the table

        Args:
            symbol (str): the symbol to add
            address (int): the address to add

        """
        if self.validate_symbol(symbol):
            self.symbol_table[symbol] = address
        else:
            raise ValueError(f"Invalid symbol. Must not have @, (, or ): {symbol}")

    def validate_symbol(self, symbol: str) -> bool:
        """
        Checks if the symbol has no "@" or "(" or ")"

        Args:
            symbol (str): the symbol to check

        Returns:
            bool: True if the symbol is valid, False otherwise
        """
        return "@" not in symbol and "(" not in symbol and ")" not in symbol
    def contains(self, symbol: str) -> bool:
        """
        Checks if the symbol table contains the given symbol

        Args:
            symbol (str): the symbol to check

        Returns:
            bool: True if the symbol is in the table, False otherwise
        """
        return symbol in self.symbol_table.keys()

    def getAddress(self, symbol: str) -> int:
        """
        Get the address associated with the symbol

        Args:
            symbol (str): the symbol to get the address of

        Returns:
            int: the address associated with the symbol
        """
        if not self.validate_symbol(symbol):
            raise ValueError(f"Invalid symbol. Must not have @, (, or ): {symbol}")
        if self.contains(symbol):   
            return self.symbol_table[symbol]
        else:
            raise ValueError(f"Symbol not found: {symbol}")
