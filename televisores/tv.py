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
