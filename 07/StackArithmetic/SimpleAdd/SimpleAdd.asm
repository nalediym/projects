
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
            

                // get x 
                
                @SP
                M=M-1
            
                // set x
                @SP
                D=M
                // get y
                
                @SP
                M=M-1
            
                // add x and y
                @SP
                D=D+M
                // set result
                @result
                M=D
                // push result to stack
                @result
                D=M
                @SP
                A=M
                M=D
                
                @SP
                M=M+1
            
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        