// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// get R0
@R0
D=M // D = RAM[0]
@i
M=D // i = RAM[0]
@sum
M=0 // sum = 0
(LOOP)
    // if i == 0, end
    @i 
    D=M // D = RAM[i]
    @STOP
    D;JEQ // if D == 0, jump to STOP
    // sum = sum + RAM[1] = sum + R1
    @R1
    D=M // D = RAM[1]
    @sum
    M=D+M // sum = sum + RAM[1]
    // i = i - 1
    @i
    M=M-1 // i = i - 1
    @LOOP
    0;JMP // jump to LOOP

(STOP)
    // store R2
    @sum
    D=M // D = RAM[sum]
    @R2
    M=D // RAM[2] = RAM[sum] 
(END)
    @END
    0;JMP // infinite loop to end cleanly 