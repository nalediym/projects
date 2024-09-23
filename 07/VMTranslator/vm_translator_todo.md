# VM Translator Project Todo List

## Today's Work Review
- [x] Added `COMMAND` attribute to each Enum class in `vm_templates.py`
- [x] Updated `CodeWriter` class to use the new `COMMAND` attributes
- [x] Implemented command handlers in `CodeWriter` for push, pop, and arithmetic operations
- [x] Created a `Segment` dataclass to represent memory segments

## Next Steps
- [ ] Implement the `write_pop` method in `CodeWriter` 
- [ ] Complete the `write_push` method for all segment types
- [ ] Implement the `write_arithmetic` method for all arithmetic operations
- [ ] Create template files for each push, pop, and arithmetic operation
  - [ ] Create push template files:
    - [ ] push_constant.asm
    - [ ] push_local.asm
    - [ ] push_argument.asm
    - [ ] push_this.asm
    - [ ] push_that.asm
    - [ ] push_temp.asm
    - [ ] push_pointer.asm
    - [ ] push_static.asm
  - [ ] Create pop template files:
    - [ ] pop_local.asm
    - [ ] pop_argument.asm
    - [ ] pop_this.asm
    - [ ] pop_that.asm
    - [ ] pop_temp.asm
    - [ ] pop_pointer.asm
    - [ ] pop_static.asm
  - [ ] Create arithmetic template files:
    - [ ] add.asm
    - [ ] sub.asm
    - [ ] neg.asm
    - [ ] eq.asm
    - [ ] gt.asm
    - [ ] lt.asm
    - [ ] and.asm
    - [ ] or.asm
    - [ ] not.asm
  - [ ] Ensure all template files use placeholders for dynamic values (e.g., $index, $segment)
  - [ ] Test each template file individually to verify correct assembly code generation
- [ ] Write unit tests for `CodeWriter` methods
- [ ] Implement error handling for invalid commands or segments
- [ ] Create a main `VMTranslator` class that uses `Parser` and `CodeWriter`
- [ ] Test the complete VM translator with sample VM code files
- [ ] Optimize the code generation process if needed
- [ ] Add comments and docstrings to improve code readability
- [ ] Consider implementing support for function calls and program flow commands

## Relevant Files
- `07/VMTranslator/vm_templates.py`
- `07/VMTranslator/code_writer.py`
- `07/StackArithmetic/SimpleAdd/SimpleAdd.vm`
- `07/VMTranslator/constant.asm`
- `07/StackArithmetic/SimpleAdd/SimpleAdd.asm`
- `07/VMTranslator/test_vm_translator.py`
- `07/VMTranslator/parser.py`
- `04/fill/Fill.tst`
- `04/fill/FillAutomatic.cmp`
- `04/fill/FillAutomatic.tst`

## Notes
- Remember to tackle these tasks one at a time
- Test your implementation as you progress
- Refer to the relevant files when working on specific components