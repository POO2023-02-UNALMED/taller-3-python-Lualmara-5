class TV:

    numTV = 0
    
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.precio = 500
        self.control = None
        self.volumen = 1
        TV.numTV += 1
    
    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca
    
    def setCanal(self, canal):
        if ((self.estado == True) and (canal>=1 and canal<=120)):
            self.canal = canal

    def getCanal(self):
        return self.canal
    
    def setPrecio(self, precio):
        self.precio = precio

    def getPrecio(self):
        return self.precio
    
    def setControl(self, control):
        self.control = control

    def getControl(self):
        return self.control
    
    def setVolumen(self, volumen):
        if ((self.estado == True) and (volumen>=0 and volumen<=7)):
            self.volumen = volumen

    def getVolumen(self):
        return self.volumen
    
    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if((self.estado == True)) and (self.canal>=1 and self.canal<120):
            self.canal += 1

    def canalDown(self):
        if((self.estado == True) and (self.canal>1 and self.canal<=120)):
            self.canal -= 1
    
    def volumenUp(self):
        if((self.estado == True) and (self.volumen>=0 and self.volumen<7)):
            self.volumen += 1

    def volumenDown(self):
        if((self.estado == True) and (self.volumen>0 and self.volumen<=7)):
            self.volumen -= 1

    @classmethod
    def setNumTV(cls, numTV):
        cls.numTV = numTV

    @classmethod
    def getNumTV(cls):
        return cls.numTV