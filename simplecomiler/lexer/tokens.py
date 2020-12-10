class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value


class Punctuation(Token):
    def _init_(self, value):
        super().__init__('punc', value)


class Number(Token):
    def _init_(self, value):
        super().__init__('num', value)


class String(Token):
    def __init__(self, value):
        super().__init__('str', value)


class Keyword(Token):
    def __init__(self, value):
        super().__init__('kw', value)


class Variable(Token):
    def __init__(self, value):
        super().__init__('var', value)


class Operator(Token):
    def __init__(self, value):
        super().__init__('op', value)
