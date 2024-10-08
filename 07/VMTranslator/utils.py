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

ASM_PSEUDO_CODE = {
    'add': {'RESULT': 'M=D+M'},
    'sub': {'RESULT': 'M=M-D'},
    'neg': {'RESULT': 'M=-M'},
    'eq': {'RESULT': 'M=D-M', 'TRUE': 'D;JEQ', 'FALSE': 'D;JNE'},
    'gt': {'RESULT': 'M=D-M', 'END': 'D;JGT'},
    'lt': {'RESULT': 'M=D-M', 'END': 'D;JLT'},
    'and': {'RESULT': 'M=D&M'},
    'or': {'RESULT': 'M=D|M'},
    'not': {'RESULT': 'M=!M'}, 
    'SP--': {'RESULT': 'M=M-1'},
    'SP++': {'RESULT': 'M=M+1'},
}
    