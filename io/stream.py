class InputStream:
    class StreamPosition:
        def __init__(self, line, col):
            self.line = line
            self.col = col

        def __str__(self):
            return f'line: {self.line}, col: {self.col}'

        def __repr__(self):
            return self.__str__()

    def __init__(self, file_name, stream_encoding='utf-8'):
        self.file_name = file_name
        self.fd = None
        self.pos = 0
        self.line = 1
        self.col = 0
        self.stream_encoding = stream_encoding

    def __enter__(self):
        self.init()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fd:
            self.fd.close()

    def init(self):
        self.fd = open(self.file_name, 'r')

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

    def eof(self):
        return self.peek() == ''

    def croak(self, msg):
        raise Exception(msg)

    def close(self):
        if self.fd:
            self.fd.close()

    def _read_single_character(self):
        return self.fd.read(1).decode(self.stream_encoding)

    def current_position(self):
        return InputStream.StreamPosition(self.line, self.col)
