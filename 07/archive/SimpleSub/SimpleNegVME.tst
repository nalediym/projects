// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/StackArithmetic/neg/negVME.tst

load neg.vm,
output-file neg.out,
compare-to neg.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set RAM[0] 256,  // initializes the stack pointer

repeat 3 {       // neg.vm has 3 instructions
  vmstep;
}

output;          // the stack pointer and the stack base
