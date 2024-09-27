// add
// return value : x + y 
// return type : int

// Each arithmetic/logical command pops 
// one or two values from the stack, 
// computes one of these functions on these 
// values, and pushes the computed value 
// onto the stack

// pop x
// pop y
// add
// push result

// pop x --> RAM[SP] = x
// pop y --> RAM[SP] = y

// initialize x
@SP
AM=M-1 // Decrement SP and point to top of stack
D=M   // D = second operand (8) 
@x // A = x
D=A // D = x
// initialize y
@y // A = y
D=A // D = y

// add x and y
@y // A = y
D=D+A
@z // A = z
M=D 