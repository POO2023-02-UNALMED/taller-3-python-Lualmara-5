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
