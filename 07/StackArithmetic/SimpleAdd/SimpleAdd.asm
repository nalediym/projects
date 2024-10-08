
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
            

                // get x from stack
                @SP
                M=M-1
                A=M
                D=M
                @x
                M=D
        
                // get y from stack
                @SP
                M=M-1
                A=M
                D=M
                @y
                M=D
        
                @x
                D=M
                @y
                D=D+M
                @result
                M=D
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        