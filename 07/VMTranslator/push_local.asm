// push local i
// addr <-- LCL + i
    @LCL // A = LCL = 1
    D=A // D = LCL = 1
    @i // A = i = 2 
    M=A // M = i = 2 = RAM[2]
    @addr // addr <-- LCL + index <-- D + M
    M=D+M // M = 1 + 2 = 3 = RAM[3]
// SP-- --> SP = SP - 1
    @SP // A = SP // A = 0
    A = A - 1 // A = SP - 1 = 15 - 1 = 14
// RAM[addr] <-- RAM[SP] // RAM[3] <-- RAM[14] //
    @addr
    D=M // D = RAM[3] = 3
    @SP
    M=D // RAM[SP] = 3