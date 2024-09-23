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

        if carrier == 'T-Mobile':
            self.dataIncrement = 1
            self.vvmIncrement = 2
            self.mmsIncrement = 4

    def getTypemask(self):
        if self.vvmEnabled:
            self.typemask += self.vvmIncrement
        if self.dataEnabled:
            self.typemask += self.dataIncrement
        if self.mmsEnabled:
            self.typemask += self.mmsIncrement

        return self.typemask

    def toggleVVM(self):
        if self.vvmEnabled:
            self.vvmEnabled = False
        else:
            self.vvmEnabled = True

    def toggleMMS(self):
        if self.mmsEnabled:
            self.mmsEnabled = False
        else:
            self.mmsEnabled = True

    def toggleData(self):
        if self.dataEnabled:
            self.dataEnabled = False
        else:
            self.dataEnabled = True