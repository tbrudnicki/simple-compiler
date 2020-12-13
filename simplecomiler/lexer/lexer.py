from contextlib import contextmanager

from simplecomiler.lexer.tokens import *


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
        while (not input_stream.eof()) and input_stream.peek().isspace():
            input_stream.next()
        return None


class CommentHandler:

    def __init__(self, comment_char='#'):
        self.comment_char = comment_char

    def handle(self, input_stream):
        input_stream.next()
        while (not input_stream.eof()) and input_stream.next() != '\n':
            pass
        return None

    def can_handle(self, input_stream):
        return input_stream.peek() == '#'


class PunctuationHandler:
    def __init__(self, punctuation_signs=[",", ":", "(", ")"]):
        self.punctuation_signs = punctuation_signs

    def can_handle(self, input_stream):
        return input_stream.peek() in self.punctuation_signs

    def handle(self, input_stream):
        return Punctuation(input_stream.next())


class StringHandler:

    def __init__(self):
        pass

    def can_handle(self, input_stream):
        return input_stream.peek() == '"'

    def handle(self, input_stream):
        input_stream.next()
        aggregate = []
        while not input_stream.eof():
            next_element = input_stream.next()
            if next_element == '"':
                return String(''.join(aggregate))
            aggregate.append(next_element)

        raise input_stream.croak('Not enclosed string at ' + input_stream.current_position())


'''
1
1.0
-1
-1.023
1.0E-9
10E6
errors
-1.023.
'''


class NumberHandler:
    INITIAL = 'initial'
    FRACTION = 'fraction'
    SCIENTIFIC = 'scientific'

    def __init__(self):
        self.state = NumberHandler.INITIAL

    def can_handle(self, input_stream):
        stream_lookup = input_stream.peek()
        return stream_lookup.isnumeric() or stream_lookup == '-'

    def handle(self, input_stream):
        aggregate = input_stream.next()

        def handle_fraction():
            while not input_stream.eof() and input_stream.peek().isnumeric():
                aggregate.append(input_stream.next())
            self.state = NumberHandler.FRACTION

        def handle_scientific_notation():
            while not input_stream.eof() and (input_stream.peek().isnumeric() or input_stream.peek() == '-'):
                aggregate.append(input_stream.next())
            self.state = NumberHandler.SCIENTIFIC

        while not input_stream.eof():
            stream_lookup = input_stream.peek()
            if stream_lookup.isnumeric():
                aggregate.append(input_stream.next())
            elif stream_lookup == '.':
                if self.state in [NumberHandler.INITIAL]:
                    aggregate.append(input_stream.next())
                    handle_fraction()
                else:
                    break
            elif stream_lookup in ['e', 'E']:
                if self.state in [NumberHandler.INITIAL, NumberHandler.FRACTION]:
                    handle_scientific_notation()
                else:
                    break

        return Number(''.join(aggregate))


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
