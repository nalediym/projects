// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/StackArithmetic/add/addVME.tst

load add.vm,
output-file add.out,
compare-to add.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set RAM[0] 256,  // initializes the stack pointer

repeat 3 {       // add.vm has 3 instructions
  vmstep;
}

output;          // the stack pointer and the stack base
