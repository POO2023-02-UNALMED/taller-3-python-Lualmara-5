from televisores.tv import TV
class Control:
    def __init__(self):
        self.tv = None
    
    def setTv(self, tv):
           self.tv = tv
    def getTv(self):
           return self.tv

    def enlazar(self, tv):
        self.tv = tv
        self.tv.setControl(self)
    
    def turnOn(self):
            self.tv.turnOn()
    def turnOff(self):
            self.tv.turnOff()
    
    def canalUp(self):
            self.tv.canalUp()
    def canalDown(self):
            self.tv.canalDown()
    
    def volumenDown(self):
            self.tv.volumenDown()
    def volumenUp(self):
            self.tv.volumenUp()
    
    def setCanal(self,canal):
            self.tv.setCanal(canal)
    def setVolumen(self, volumen):
            self.tv.setVolumen(volumen)