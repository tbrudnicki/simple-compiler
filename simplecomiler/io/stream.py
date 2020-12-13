from io import StringIO


class AbstractInputStream:
    class StreamPosition:
        def __init__(self, line, col):
            self.line = line
            self.col = col

        def __str__(self):
            return f'line: {self.line}, col: {self.col}'

        def __repr__(self):
            return self.__str__()

    def __init__(self):
        self.pos = 0
        self.line = 1
        self.col = 0

    def current_position(self):
        return AbstractInputStream.StreamPosition(self.line, self.col)

    def peek(self):
        raise Exception('Invoking abstract method')

    def next(self):
        raise Exception('Invoking abstract method')

    def eof(self):
        return self.peek() == ''

    def croak(self, message):
        raise Exception(message)


def file_is(file_descriptor):
    class FileInputStream(AbstractInputStream):

        def __init__(self, stream):
            self.fd = stream

        def peek(self):
            current_position = self.fd.tell()
            c = self._read_single_character()
            self.fd.seek(current_position)
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
            return self.fd.read(1).decode(self.stream_encoding)

    return FileInputStream(file_descriptor)


def string_is(input_string):
    class StringInputStream(AbstractInputStream):
        def __init__(self, string_stream):
            self.text_stream = string_stream

        def peek(self):
            current_position = self.text_stream.tell()
            result = self.text_stream.read(1)
            self.text_stream.seek(current_position)
            return result

        def next(self):
            return self.text_stream.read(1)

    return StringInputStream(StringIO(input_string))
