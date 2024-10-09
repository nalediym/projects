class Memory:
    def __init__(self):
        self.memory = {}

    def read(self, address):
        return self.memory.get(address, 0)

    def write(self, address, value):
        self.memory[address] = value

class Stack(Memory):
    def __init__(self):
        super().__init__()
        self.sp = 0

    def push(self, value):
        self.write(self.sp, value)
        self.sp += 1

    def pop(self):
        self.sp -= 1
        return self.read(self.sp)

class RAM(Memory):
    pass

class Registers(RAM, Stack):
    def __init__(self):
        super().__init__()
        self.register_names = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11', 'R12', 'R13', 'R14', 'R15']

    def read_register(self, register_name):
        if register_name in self.register_names:
            return self.read(self.register_names.index(register_name))
        raise ValueError(f"Invalid register name: {register_name}")

    def write_register(self, register_name, value):
        if register_name in self.register_names:
            self.write(self.register_names.index(register_name), value)
        else:
            raise ValueError(f"Invalid register name: {register_name}")