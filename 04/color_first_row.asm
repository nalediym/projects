// color the whole row black
@32
D=A
@cols
M=D

@SCREEN
D=A // D = SCREEN
@address
M=D // address = SCREEN = 16384

(LOOP)
    @address
    A=M // set address to current address
    M=-1 // set pixels to black
    @address
    M=M+1 // address = address + 1 
    @cols
    M=M-1 // cols = cols - 1
    
    @LOOP
    D;JGT // if cols > 0, continue loop
