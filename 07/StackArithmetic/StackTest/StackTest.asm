
                @17
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
            

                @17
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
                D=M
                @x
                M=D
        
                // get y from stack
                @SP
                M=M-1
                D=M
                @y
                M=D
        
                @x
                D=M
                @y
                D=D-M
                @true1
                D;JEQ // if x == y
                @false1
                D;JNE // if x != y
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
        

                @17
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
            

                @16
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
                D=M
                @x
                M=D
        
                // get y from stack
                @SP
                M=M-1
                D=M
                @y
                M=D
        
                @x
                D=M
                @y
                D=D-M
                @true2
                D;JEQ // if x == y
                @false2
                D;JNE // if x != y
                (true2)
                @result
                M=-1
                (false2)
                @result
                M=0
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        

                @16
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
            

                @17
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
                D=M
                @x
                M=D
        
                // get y from stack
                @SP
                M=M-1
                D=M
                @y
                M=D
        
                @x
                D=M
                @y
                D=D-M
                @true3
                D;JEQ // if x == y
                @false3
                D;JNE // if x != y
                (true3)
                @result
                M=-1
                (false3)
                @result
                M=0
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        

                @892
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
            

                @891
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
                D=M
                @x
                M=D
        
                // get y from stack
                @SP
                M=M-1
                D=M
                @y
                M=D
        
                @x
                D=M
                @y
                D=D-M
                @true4
                D;JLT // if x < y
                @false4
                D;JGE // if x >= y
                (true4)
                @result
                M=-1
                (false4)
                @result
                M=0
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        

                @891
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
            

                @892
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
                D=M
                @x
                M=D
        
                // get y from stack
                @SP
                M=M-1
                D=M
                @y
                M=D
        
                @x
                D=M
                @y
                D=D-M
                @true5
                D;JLT // if x < y
                @false5
                D;JGE // if x >= y
                (true5)
                @result
                M=-1
                (false5)
                @result
                M=0
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        

                @891
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
            

                @891
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
                D=M
                @x
                M=D
        
                // get y from stack
                @SP
                M=M-1
                D=M
                @y
                M=D
        
                @x
                D=M
                @y
                D=D-M
                @true6
                D;JLT // if x < y
                @false6
                D;JGE // if x >= y
                (true6)
                @result
                M=-1
                (false6)
                @result
                M=0
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        

                @32767
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
            

                @32766
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
                D=M
                @x
                M=D
        
                // get y from stack
                @SP
                M=M-1
                D=M
                @y
                M=D
        
                @x
                D=M
                @y
                D=D-M
                @true7
                D;JGT // if x > y
                @false7
                D;JLE // if x <= y
                (true7)
                @result
                M=-1
                (false7)
                @result
                M=0
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        

                @32766
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
            

                @32767
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
                D=M
                @x
                M=D
        
                // get y from stack
                @SP
                M=M-1
                D=M
                @y
                M=D
        
                @x
                D=M
                @y
                D=D-M
                @true8
                D;JGT // if x > y
                @false8
                D;JLE // if x <= y
                (true8)
                @result
                M=-1
                (false8)
                @result
                M=0
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        

                @32766
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
            

                @32766
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
                D=M
                @x
                M=D
        
                // get y from stack
                @SP
                M=M-1
                D=M
                @y
                M=D
        
                @x
                D=M
                @y
                D=D-M
                @true9
                D;JGT // if x > y
                @false9
                D;JLE // if x <= y
                (true9)
                @result
                M=-1
                (false9)
                @result
                M=0
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        

                @57
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
            

                @31
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
            

                @53
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
                D=M
                @x
                M=D
        
                // get y from stack
                @SP
                M=M-1
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
        

                @112
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
                D=M
                @x
                M=D
        
                // get y from stack
                @SP
                M=M-1
                D=M
                @y
                M=D
        
                @x
                D=M
                @y
                D=D-M
                @result
                M=D
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        

                // get y from stack
                @SP
                M=M-1
                D=M
                @y
                M=D
        
                @y
                D=M
                @result
                M=-D
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        

                // get x from stack
                @SP
                M=M-1
                D=M
                @x
                M=D
        
                // get y from stack
                @SP
                M=M-1
                D=M
                @y
                M=D
        
                @x
                D=M
                @y
                D=D&M
                @true13
                D;JGE // if x & y >= 1 // if 1 & 1  
                @false13
                D;JLT // if x & y == 0 // if 0 & 0
                (true13)
                @result
                M=-1
                (false13)
                @result
                M=0
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        

                @82
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
                D=M
                @x
                M=D
        
                // get y from stack
                @SP
                M=M-1
                D=M
                @y
                M=D
        
                @x
                D=M 
                @y
                D=D|M
                @true14
                D;JGE // if x | y >= 1 // if 1 | 1
                @false14
                D;JLT // if x | y == 0 // if 0 | 0
                (true14)
                @result
                M=-1
                (false14)
                @result
                M=0
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        

                // get x from stack
                @SP
                M=M-1
                D=M
                @x
                M=D
        
                @x
                D=M 
                @true15
                D;JEQ // if x == 0
                @false15
                D;JNE // if x != 0
                (true15)
                @result
                M=-1
                (false15)
                @result
                M=0
        
                @result
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
        