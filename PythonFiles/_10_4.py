class MessreiheEigenIter:
    def __init__(self, messreihe):
        self.messreihe = messreihe
        self.pos = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.pos += 1
        if self.pos >= len(self.messreihe):
            raise StopIteration
        return list(self.messreihe)[self.pos]

