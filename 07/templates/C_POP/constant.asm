// push constant index
@index // D = index
D=A
@SP // A = SP
A=M // A = RAM[SP]
M=D // RAM[A] = D
@SP // A = SP   
M=M+1 // RAM[SP] = RAM[SP] + 1