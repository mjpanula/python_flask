class MySingleStringHolder:
    def __init__(self, string):
        self.string = string
    def get(self):
        return self.string
    def set(self, string):
        self.string = string