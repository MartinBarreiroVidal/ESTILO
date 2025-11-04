#Ejercicio 1 (falta un espacio entre el "#" e la palabra "Ejercicio".
temperatura1 = int(input("Introduce a temperatura del día 1 en grados celsius: ")) # Usar nombres más descriptivos y claros para las variables.
temperatura2 = int(input("Introduce a temperatura del día 2 en grados celsius: "))
temperatura3 = int(input("Introduce a temperatura del día 3 en grados celsius: "))
temperatura4 = int(input("Introduce a temperatura del día 4 en grados celsius: "))
temperatura5 = int(input("Introduce a temperatura del día 5 en grados celsius: "))
temperatura6 = int(input("Introduce a temperatura del día 6 en grados celsius: "))
temperatura7 = int(input("Introduce a temperatura del día 7 en grados celsius: "))
listaTemperaturas = (temperatura1,temperatura2,temperatura3,temperatura4,temperatura5,temperatura6,temperatura7) # Usar nombres de variables más claros y descriptivos.

#Ejercicio 2
media = sum(listaTemperaturas) / 7
print("La temperatura media es de",media,"grados")

#Ejercicio 3
def calculoDias(contador):
    contador = 0
    if valor > media: # Poner espacios entre los valores y el signo.
        contador = contador + 1
    print("El total de días en los que la temperatura estubo por encima de la media fue de",contador)
print(calculoDias(contador))

#Ejercicio 4
for valor in listaTemperaturas:
    if valor>media:
        if valor == temperatura1: # En los print tendremos que aplicar la regla de los >79 caracteres, hay que hacerlo más corto.
            print(
                "El lunes la temperatura estuvo por encima de la media "
                "ya que ese día hizo", temperatura1, "grados"
            )

        elif valor == temperatura2:
            print(
                "El martes la temperatura estuvo por encima de la media "
                "ya que ese día hizo", temperatura1, "grados"
            )

        elif valor == temperatura3:
            print(
                "El miércoles la temperatura estuvo por encima de la media "
                "ya que ese día hizo", temperatura1, "grados"
            )
        elif valor == temperatura4:
            print(
                "El jueves la temperatura estuvo por encima de la media "
                "ya que ese día hizo", temperatura1, "grados"
            )
        elif valor == temperatura5:
            print(
                "El viernes la temperatura estuvo por encima de la media "
                "ya que ese día hizo", temperatura1, "grados"
            )
        elif valor == temperatura6:
            print(
                "El sabado la temperatura estuvo por encima de la media "
                "ya que ese día hizo", temperatura1, "grados"
            )
        elif valor == temperatura7:
            print((
                "El domingo la temperatura estuvo por encima de la media "
                "ya que ese día hizo", temperatura1, "grados"
            ))
