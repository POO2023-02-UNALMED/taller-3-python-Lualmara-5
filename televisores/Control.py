class Control:
    def __init__(self):
        self._tv = None

    def enlazar(self, tv):
        tv.setControl(self)
        self.setTv(tv)

    def getTv(self):
        return self._tv
    
    def setTv(self, tv):
        self._tv = tv

    def turnOn(self):
        if self._tv != None:
            self._tv.turnOn()

    def turnOff(self):
        if self._tv != None:
            self._tv.turnOff() 

    def canalUp(self):
        if self._tv != None:
            self._tv.canalUp()

    def canalDown(self):
        if self._tv != None:
            self._tv.canalDown()

    def volumenUp(self):
        if self._tv != None:
            self._tv.volumenUp()

    def volumenDown(self):
        if self._tv != None:
            self._tv.volumenDown()

    def setCanal(self, canal):
        if self._tv != None:
            self._tv.setCanal(canal)
        
    def setVolumen(self, volumen):
        if self._tv != None:
            self._tv.setVolumen(volumen)