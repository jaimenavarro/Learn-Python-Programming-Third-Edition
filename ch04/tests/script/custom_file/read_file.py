def test():
    print("Testing")


class ReadFile:
    def __init__(self, path):
        self.path = path
        self.file = open(path, 'rt')

    def read_line(self):
        return self.file.readline()

    def close(self):
        self.file.close()
