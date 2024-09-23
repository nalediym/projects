import os
from enum import Enum, auto
from string import Template
from typing import Dict, Callable

class TemplateType(Enum):
    PUSH = auto()
    POP = auto()
    ARITHMETIC = auto()

class PushTemplate(Enum):
    COMMAND = 'C_PUSH'
    CONSTANT = 'constant'
    LOCAL = 'local'
    ARGUMENT = 'argument'
    THIS = 'this'
    THAT = 'that'

class PopTemplate(Enum):
    COMMAND = 'C_POP'
    LOCAL = 'local'
    ARGUMENT = 'argument'
    THIS = 'this'
    THAT = 'that'

class ArithmeticTemplate(Enum):
    COMMAND = 'C_ARITHMETIC'
    ADD = 'add'
    SUB = 'sub'
    NEG = 'neg'
    EQ = 'eq'
    GT = 'gt'
    LT = 'lt'
    AND = 'and'
    OR = 'or'
    NOT = 'not'

class VMTemplates:
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    templates: Dict[str, Template] = {}

    @classmethod
    def get_template(cls, template_type: TemplateType, template_enum: Enum) -> Callable[[Dict[str, str]], str]:
        template_name = f"{template_type.name.lower()}_{template_enum.value}"
        if template_name not in cls.templates:
            file_path = os.path.join(cls.template_dir, f"{template_name}.asm")
            with open(file_path, 'r') as file:
                cls.templates[template_name] = Template(file.read().strip())
        
        def render(context: Dict[str, str]) -> str:
            return cls.templates[template_name].safe_substitute(context)
        
        return render