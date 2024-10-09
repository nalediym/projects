
                @7
                D=A
                @addr
                M=D // RAM[addr] = index
            
                @addr
                D=M 
                @SP 
                A=M
                M=D // RAM[SP] = D
                @SP
                M=M+1 // SP++
            

                @8
                D=A
                @addr
                M=D // RAM[addr] = index
            
                @addr
                D=M 
                @SP 
                A=M
                M=D // RAM[SP] = D
                @SP
                M=M+1 // SP++
            

                @x
                D=M 
                @y
                D=D|M
                @true1
                D;JGE // if x | y >= 1 // if 1 | 1
                @false1
                D;JLT // if x | y == 0 // if 0 | 0
                (true1)
                @result
                M=-1
                (false1)
                @result
                M=0
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        