class RAM:
    """
    RAM is a class that represents the RAM of the computer.
    """
    def __init__(self):
        self.memory = {}
        self.stack = Stack()

    def get(self, address: int) -> int:
        return self.memory.get(address, 0)
    
class Register(dict):
    """
    Register is a class that represents the register of the computer.
    """
    def __init__(self):
        self.index = 0
        self.symbol_name = ""

    def get(self, address: int) -> int:
        return self.memory.get(address, 0)
    
class Stack:
    """
    Stack is a class that represents the stack of the computer.
    Stack is a part of the RAM class.
    
    """
    def __init__(self):
        self.memory = []

    def push(self, value: int):
        self.memory.append(value)
        