import unittest
from HackAssembler.Code import Code

class TestCode(unittest.TestCase):
    def setUp(self):
        pass

    def test_comp(self):
        code = Code()
        self.assertEqual(code.comp("A+1"), "0110111")
        self.assertEqual(code.comp("D&M"), "1000000")

        # test invalid comp fields
        with self.assertRaises(ValueError):
            code.comp("A+1000")
        with self.assertRaises(ValueError):
            code.comp("D&M+1")  
        with self.assertRaises(ValueError):
            code.comp("@100")
        with self.assertRaises(ValueError):
            code.comp("@SP")

    def test_dest(self):
        # dest("DM") returns "011"
        code = Code()
        self.assertEqual(code.dest("DM"), "011")

        # test invalid dest fields
        with self.assertRaises(ValueError):
            code.dest("DM+1")
        with self.assertRaises(ValueError):
            code.dest("D&M")
        with self.assertRaises(ValueError):
            code.dest("A+D")

    def test_jump(self):
        # jump("JMP") returns "111"
        code = Code()
        self.assertEqual(code.jump("JNE"), "101")

        # test invalid jump fields
        with self.assertRaises(ValueError):
            code.jump("JMP+1")
        with self.assertRaises(ValueError):
            code.jump("D&M")


    def test_validate_comp_field(self):
        code = Code()
        self.assertTrue(code._validate_comp_field("A+1"))
        self.assertTrue(code._validate_comp_field("D&M"))
        self.assertFalse(code._validate_comp_field("A+1000"))
        self.assertFalse(code._validate_comp_field("D&M+1"))
        self.assertFalse(code._validate_comp_field("@100"))
        self.assertFalse(code._validate_comp_field("@SP"))  

    def test_validate_dest_field(self):
        code = Code()
        self.assertTrue(code._validate_dest_field("M"))
        self.assertTrue(code._validate_dest_field("D"))
        self.assertTrue(code._validate_dest_field("MD"))
        self.assertTrue(code._validate_dest_field("A"))
        self.assertTrue(code._validate_dest_field("AM"))
        self.assertTrue(code._validate_dest_field("AD"))
        self.assertTrue(code._validate_dest_field("AMD"))
        self.assertFalse(code._validate_dest_field("DM+1"))
        self.assertFalse(code._validate_dest_field("D&M"))
        self.assertFalse(code._validate_dest_field("A+D"))

    def test_validate_jump_field(self):
        code = Code()
        self.assertTrue(code._validate_jump_field("JMP"))
        self.assertTrue(code._validate_jump_field("JNE"))
        self.assertTrue(code._validate_jump_field("JLT"))
        self.assertTrue(code._validate_jump_field("JGE"))
        self.assertTrue(code._validate_jump_field("JGT"))
        self.assertTrue(code._validate_jump_field("JLE"))
        self.assertTrue(code._validate_jump_field("JEQ"))
        self.assertFalse(code._validate_jump_field("JMP+1"))
        self.assertFalse(code._validate_jump_field("D&M"))