// push constant 7
@7 
D=A // D = 7
@SP 
A=M // A = RAM[SP]
M=D // M = RAM[SP] = D = 7 
@SP
M=M+1 // M = 7 + 1 = 8
// push constant 8
@8 
D=A // D = 8 
@SP
A=M // A = RAM[SP]
M=D // M = 8 
@SP
M=M+1 // M = 9 
// add
@SP
AM=M-1 // Decrement SP and point to top of stack
D=M   // D = second operand (8)
@SP
AM=M-1 // Decrement SP and point to first operand
M=D+M  // Add first and second operands (7+8)
@SP
M=M+1  // Increment SP
