#Ejercicio 1 (falta un espacio entre el "#" e la palabra "Ejercicio".
temperaturaLunes = int(input("Introduce a temperatura del día 1 en grados celsius: ")) # Usar nombres más descriptivos y claros para las variables.
temperaturaMartes = int(input("Introduce a temperatura del día 2 en grados celsius: "))
temperaturaMiercoles = int(input("Introduce a temperatura del día 3 en grados celsius: "))
temperaturaJueves = int(input("Introduce a temperatura del día 4 en grados celsius: "))
temperaturaViernes = int(input("Introduce a temperatura del día 5 en grados celsius: "))
temperaturaSabado = int(input("Introduce a temperatura del día 6 en grados celsius: "))
temperaturaDomingo = int(input("Introduce a temperatura del día 7 en grados celsius: "))
listaTemperaturas = (temperaturaLunes,temperaturaMartes,temperaturaMiercoles,temperaturaJueves,temperaturaViernes,temperaturaSabado,temperaturaDomingo) # Usar nombres de variables más claros y descriptivos.

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
        if valor == temperaturaLunes: # En los print tendremos que aplicar la regla de los >79 caracteres, hay que hacerlo más corto.
            print(
                "El lunes la temperatura estuvo por encima de la media "
                "ya que ese día hizo", temperaturaLunes, "grados"
            )

        elif valor == temperaturaMartes:
            print(
                "El martes la temperatura estuvo por encima de la media "
                "ya que ese día hizo", temperaturaLunes, "grados"
            )

        elif valor == temperaturaMiercoles:
            print(
                "El miércoles la temperatura estuvo por encima de la media "
                "ya que ese día hizo", temperaturaLunes, "grados"
            )
        elif valor == temperaturaJueves:
            print(
                "El jueves la temperatura estuvo por encima de la media "
                "ya que ese día hizo", temperaturaLunes, "grados"
            )
        elif valor == temperaturaViernes:
            print(
                "El viernes la temperatura estuvo por encima de la media "
                "ya que ese día hizo", temperaturaLunes, "grados"
            )
        elif valor == temperaturaSabado:
            print(
                "El sabado la temperatura estuvo por encima de la media "
                "ya que ese día hizo", temperaturaLunes, "grados"
            )
        elif valor == temperaturaDomingo:
            print((
                "El domingo la temperatura estuvo por encima de la media "
                "ya que ese día hizo", temperaturaLunes, "grados"
            ))
