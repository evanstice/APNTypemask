class Typemask:
    def __init__(self):
        self.typemask = 0
        self.vvmEnabled = False
        self.dataEnabled = False
        self.mmsEnabled = False

    def getTypemask(self):
        if self.vvmEnabled == True:
            self.typemask += 0 # need to add real values