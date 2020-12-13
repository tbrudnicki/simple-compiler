from io import StringIO


class InputStream:
    class StreamPosition:
        def __init__(self, line, col):
            self.line = line
            self.col = col

        def __str__(self):
            return f'line: {self.line}, col: {self.col}'

        def __repr__(self):
            return self.__str__()

        def __eq__(self, other):
            if not isinstance(other, InputStream.StreamPosition):
                return False
            return self.line == other.line and self.col == other.col

    def __init__(self, stream):
        self.stream = stream
        self.pos = 0
        self.line = 1
        self.col = 0

    def current_position(self):
        return InputStream.StreamPosition(self.line, self.col)

    def peek(self):
        current_position = self.stream.tell()
        c = self._read_single_character()
        self.stream.seek(current_position)
        return c

    def next(self):
        current = self._read_single_character()
        self.pos += 1
        if current == '\n':
            self.line += 1
            self.col = 0
        else:
            self.col += 1
        return current

    def _read_single_character(self):
        return self.stream.read(1)

    def eof(self):
        return self.peek() == ''

    def croak(self, message):
        raise Exception(message)


def file_is(file_descriptor):
    return InputStream(file_descriptor)


def string_is(input_string):
    return InputStream(StringIO(input_string))
