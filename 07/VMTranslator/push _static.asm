// addr = { index + 16 }
@index
D=A
@16
D=D+A
@SP
A=M
D=M
@addr
M=D // RAM[addr] = RAM[SP]
