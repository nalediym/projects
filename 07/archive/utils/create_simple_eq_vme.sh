#!/bin/zsh

create_test_files() {
    local operation=$1
    local dir_name="Simple${(C)operation}"

    
    local target_dir="$HOME/Documents/Projects/nand2tetris/projects/07/archive/$dir_name"
    local source_dir="$HOME/Documents/Projects/nand2tetris/projects/07/StackArithmetic/SimpleAdd"

    # create output log files for each directory
    mkdir -p "$target_dir"
    cd "$target_dir"
    sed "s/SimpleAdd/$dir_name/g" "$source_dir/SimpleAddVME.tst" > "${dir_name}VME.tst"
    sed "s/SimpleAdd/$dir_name/g" "$source_dir/SimpleAdd.tst" > "$dir_name.tst"
    
    # create vm files for each directory
    sed "s/add/$operation/g" "$source_dir/SimpleAdd.vm" > "$dir_name.vm"
    
    # create cmp files for each directory
    cp "$source_dir/SimpleAdd.cmp" "$dir_name.cmp"

}

# create output log files for each directory


# Create test files for SimpleEq
create_test_files "eq"

# Create test files for SimpleSub
create_test_files "sub"

# List of all arithmetic operations
arithmetic_operations=(
    "add"
    "sub"
    "neg"
    "eq"
    "gt"
    "lt"
    "and"
    "or"
    "not"
)

# Create test files for all arithmetic operations
for operation in "${arithmetic_operations[@]}"; do
    create_test_files "$operation"
    # echo "Test files created for $operation."
    # echo "Test files created for $operation."
done

echo "Test files created for all arithmetic operations."
