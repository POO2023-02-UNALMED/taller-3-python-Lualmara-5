class TV:

    _numTV = 0
    def __init__(self, marca, estado):

        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        TV._numTV += 1

    def getEstado(self):
        return self._estado

    def setMarca(self, marca):
        self._marca = marca

    def getMarca(self):
        return self._marca
    
    def setCanal(self, canal):
        if self.getEstado():
            if 120>=canal>=1:
                self._canal = canal
            else:
                pass
        else:
            pass

    def getCanal(self):
        return self._canal
    
    def setPrecio(self, precio):
        self._precio = precio
    
    def getPrecio(self):
        return self._precio
    
    def setVolumen(self,volumen):
        if self.getEstado():
            if volumen <= 7 and volumen >= 0:
                self._volumen = volumen
            else:
                pass
        else:
            pass

    def getVolumen(self):
        return self._volumen
    
    def setControl(self, control):
        self._control = control

    def getControl(self):
        return self._control
    
    @classmethod
    def getNumTV(self):
        return TV._numTV
    
    @classmethod
    def setNumTV(self, numtv):
        TV._numTV = numtv

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False
    
    def canalUp(self):
        if self.getEstado():
            if self.getCanal() < 120:
                self._canal = self.getCanal() + 1
            else:
                pass
        else:
            pass

    def canalDown(self):
        if self.getEstado():
            if self.getCanal() > 1:
                self._canal = self.getCanal() - 1
            else:
                pass
        else:
            pass

    def volumenUp(self):
        if self.getEstado():
            if self.getVolumen() < 7:
                self._volumen = self.getVolumen() + 1
            else: pass
        else: 
            pass
    
    def volumenDown(self):
        if self.getEstado():
            if self.getVolumen() > 0:
                self._volumen = self.getVolumen() - 1
            else: pass
        else: 
            pass