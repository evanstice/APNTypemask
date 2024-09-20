class Typemask:
    # carriers: [1 - T-Mobile]
    def __init__(self, carrier):
        self.typemask = 0
        self.vvmEnabled = False
        self.dataEnabled = False
        self.mmsEnabled = False

        self.vvmIncrement = 0
        self.dataIncrement = 0
        self.mmsIncrement = 0

        if carrier == 1:
            self.vvmIncrement = 2
            self.dataIncrement = 1
            self.mmsIncrement = 4

    def getTypemask(self):
        if self.vvmEnabled:
            self.typemask += self.vvmIncrement
        if self.dataEnabled:
            self.typemask += self.dataIncrement
        if self.mmsEnabled:
            self.typemask += self.mmsIncrement
