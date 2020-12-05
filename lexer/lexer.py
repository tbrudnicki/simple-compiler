from contextlib import contextmanager


@contextmanager
def safe_input_stream(input_stream):
    try:
        yield input_stream
    finally:
        input_stream.close()


class WhitespaceHandler:

    def __init__(self):
        pass

    def can_handle(self, current_char):
        return current_char.isspace()

    def handle(self, input_stream):
        input_stream.next()
        while input_stream.peek().isspace():
            input_stream.next()
        return None


class Lexer:

    def __init__(self, input_stream):
        self.input = input_stream
        self.handlers = [WhitespaceHandler()]

    def lexemes_generator(self):
        character_promise = self.input.peek()
        while character_promise != '':
            candidate = next(x for x in self.handlers if x.can_handle(character_promise))
            result = candidate.handle(self.input)
            if result:
                yield result
