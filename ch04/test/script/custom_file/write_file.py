class WriteFile:
    def __init__(self, path):
        self.path = path
        self.file = open(path, 'w')

    def write_line(self, data):
        self.file.write(data)
        self.file.write('\n')
        self.file.flush()

    def close(self):
        self.file.close()
