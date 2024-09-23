// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Initialize counter for number of rows
@255
D=A // D = 255
@rows
M=D // rows = 10

// Initialize counter for number of columns
@32
D=A // D = 32
@cols
M=D // cols = 32

// Initialize screen address
@SCREEN
D=A // D = SCREEN
@address
M=D // address = SCREEN

(LOOP)
    // Set 16 pixels to black for current row
    @address
    A=M
    M=-1 // set pixels to black
    @cols
    M=M-1 // cols = cols - 1
    @LOOP
    D;JGT // if cols > 0, continue loop


    // Move to next row (add 32 to address)
    @32
    D=A // D = 32
    @address
    M=M+D // address = address + 32

    // Decrement row counter
    @rows
    MD=M-1 // rows = rows - 1

    // If rows > 0, continue loop
    @LOOP
    D;JGT // if rows > 0, continue loop


// End of loop
(END)
    @END
    0;JMP // infinite loop