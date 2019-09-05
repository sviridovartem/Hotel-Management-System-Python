class InputExceptionError(Exception):
    def __init__(self, text, num):
        self.txt = text
        self.n = num
