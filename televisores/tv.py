class TV ():
    _numTV = 0
    def __init__ (self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        TV._numTV += 1
    def getMarca (self):
        return self._marca
    def setMarca (self, marca):
        self._marca = marca
    def getCanal (self):
        return self._canal
    def setCanal (self, canal):
        if self.getEstado() and 0 < canal < 121:
            self._canal = canal
    def getPrecio (self):
        return self._precio
    def setPrecio (self, precio):
        self._precio = precio
    def getVolumen (self):
        return self._volumen
    def setVolumen (self, volumen):
        if self.getEstado() and 0 <= volumen < 8:
            self._volumen = volumen
    def getControl (self):
        return self._control
    def setControl (self, control):
        self._control = control
    @staticmethod
    def getNumTV ():
        return TV._numTV
    @staticmethod
    def setNumTV (numTV):
        TV._numTV = numTV
    def turnOn (self):
        self._estado = True
    def turnOff (self):
        self._estado = False
    def getEstado (self):
        return self._estado
    def canalUp (self):
        if self.getEstado() and self._canal < 120 and self._canal > 0:
            self._canal += 1
    def canalDown (self):
        if self.getEstado() and self._canal < 121 and self._canal > 1:
            self._canal -= 1
    def volumenUp (self):
        if self.getEstado() and self._volumen < 7 and self._volumen >= 0:
            self._volumen += 1
    def volumenDown (self):
        if self.getEstado() and 0 < self._volumen < 8:
            self._volumen -= 1