class Escuderia:
    def __init__(self):
        self.__nombre = None
        self.__motor = None
        self.__piloto = None
        self.__costoAnual = None

    @property
    def nombre(self):
        return self.__nombre

    @property
    def motor(self):
        return self.__motor

    @property
    def piloto(self):
        return self.__piloto

    @property
    def costoAnual(self):
        return self.__costoAnual

    #

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:

            print("El nombre está vacío")
        else:
            self.__nombre = nombre

    @motor.setter
    def motor(self, motor):
        if (motor != "mercedes" and motor != "ferrari" and motor != "renault" and motor != "honda"):
            print("El motor ingresado no existe")
        else:
            self.__motor = motor

    @piloto.setter
    def piloto(self, piloto):
        if not piloto:
            print("El piloto está vacío")
        else:
            self.__piloto = piloto

    @costoAnual.setter
    def costoAnual(self, costoAnual):
        if not costoAnual:
            print("El costo anual está vacío")
        else:
            self.__costoAnual = costoAnual

    def comparar(self, escuderias):
        costoMayor = escuderias[0].get('costoAnual')
        for escuderia in escuderias:
            if (escuderia.get('costoAnual') > costoMayor):
                costoMayor = escuderia.get('costoAnual')
                print(f"La escuderia más cara es: {escuderia.get('nombre')}")
        print(f" con un presupuesto de {costoMayor}")
