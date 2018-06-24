class Artist:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.__class__) + ":" + str(self.__dict__)
