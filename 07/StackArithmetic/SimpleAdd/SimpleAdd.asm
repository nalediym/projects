
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
            