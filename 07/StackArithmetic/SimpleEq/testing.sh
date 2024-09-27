grep -m1 -B2 '^\s*eq\s*$' StackTest/StackTest.vm | cat                                  

echo -e "eq\nadd" | xargs -I {} grep -m1 -B2 '^\s*{}\s*$' StackTest/StackTest.vm

ls *.vm | xargs -I{} sh -c ''grep ABC "$1" '> "$1.out"' -- {}

echo -e "eq"  | xargs -I{} sh -c 'grep -m1 -B2 "^\s*$1\s*$" StackTest/StackTest.vm > "$1.out"' -- {} 

echo -e "eq" | ls Simple{$1} 


echo -e "eq\nadd" | xargs -I{} sh -c '
  mkdir -p "Simple${1^}" &&  grep -m1 -B2 "^\s*$1\s*$" StackTest/StackTest.vm > "\"Simple${1^}\"/\"Simple${1^}\".vm"
  ' -- {}

ls /Users/naledikekana/Documents/Projects/projects/07/VMTranslator/templates/C_ARITHMETIC | xargs -n1 basename -s .asm 

ls ~/Documents/Projects/projects/07/VMTranslator/templates/C_ARITHMETIC/*.asm | xargs -n1 basename -s .asm | xargs -I {} sh -c 'grep -B2 -m1 "^{}" ../StackTest/StackTest.vm > {}.vm'  
