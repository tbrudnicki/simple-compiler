class InputStream:

    def __init__(self, file_name):
        self.file_name = file_name
        self.fd = None
        self.pos = 0
        self.line = 1
        self.col = 0

    def __enter__(self):
        self.init()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fd:
            self.fd.close()

    def init(self):
        self.fd = open(self.file_name, 'r')

    def peek(self):
        current_position = self.fd.tell()
        c = self.fd.read(1)
        self.fd.seek(current_position)
        return c

    def next(self):
        current = self.fd.read(1)
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



