// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/StackArithmetic/SimpleLt/SimpleLtVME.tst

load SimpleLt.vm,
output-file SimpleLt.out,
compare-to SimpleLt.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set RAM[0] 256,  // initializes the stack pointer

repeat 3 {       // SimpleLt.vm has 3 instructions
  vmstep;
}

output;          // the stack pointer and the stack base
