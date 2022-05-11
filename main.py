from clases.Escuderia import Escuderia

print("Escuderías de F1")
print("*****************")
opc = ()
escuderias = []

while (opc != "N"):
    escuderia = Escuderia()

    escuderia.nombre = input("Digite el nombre de la escudería: ")
    escuderia.motor = input("Digite el motor que utiliza su monoplaza: ")
    escuderia.piloto = input("Digite el nombre del piloto: ")
    escuderia.costoAnual = input(
        "Digite el presupuesto del año de su escudería: ")

    escud = dict(nombre=escuderia.nombre, motor=escuderia.motor,
                 piloto=escuderia.piloto, costoAnual=escuderia.costoAnual)
    escuderias.append(escud)

    opc = input("¿Desea agregar otra escuderia: (Y/N)")

escuderia.comparar(escuderias)
