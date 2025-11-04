#Ejercicio 1 (falta un espacio entre el "#" e la palabra "Ejercicio".
m = int(input("Introduce a temperatura del día 1 en grados celsius: "))
n = int(input("Introduce a temperatura del día 2 en grados celsius: "))
o = int(input("Introduce a temperatura del día 3 en grados celsius: "))
p = int(input("Introduce a temperatura del día 4 en grados celsius: "))
q = int(input("Introduce a temperatura del día 5 en grados celsius: "))
r = int(input("Introduce a temperatura del día 6 en grados celsius: "))
s = int(input("Introduce a temperatura del día 7 en grados celsius: "))
lista = (m,n,o,p,q,r,s) # Usar nombres de variables más claros y descriptivos.

#Ejercicio 2
media = sum(lista) / 7
print("La temperatura media es de",media,"grados")

#Ejercicio 3
def calculoDias(contador):
    contador = 0
    if valor>media:
        contador = contador + 1
    print("El total de días en los que la temperatura estubo por encima de la media fue de",contador)
print(calculoDias(contador))

#Ejercicio 4
for valor in l:
    if valor>media:
        if valor == m: # En los print tendremos que aplicar la regla de los >79 caracteres, hay que hacerlo más corto.
            print(
                "El lunes la temperatura estuvo por encima de la media "
                "ya que ese día hizo", m, "grados"
            )

        elif valor == n:
            print(
                "El martes la temperatura estuvo por encima de la media "
                "ya que ese día hizo", m, "grados"
            )

        elif valor == o:
            print(
                "El miércoles la temperatura estuvo por encima de la media "
                "ya que ese día hizo", m, "grados"
            )
        elif valor == p:
            print(
                "El jueves la temperatura estuvo por encima de la media "
                "ya que ese día hizo", m, "grados"
            )
        elif valor == q:
            print(
                "El viernes la temperatura estuvo por encima de la media "
                "ya que ese día hizo", m, "grados"
            )
        elif valor == r:
            print(
                "El sabado la temperatura estuvo por encima de la media "
                "ya que ese día hizo", m, "grados"
            )
        elif valor == s:
            print((
                "El domingo la temperatura estuvo por encima de la media "
                "ya que ese día hizo", m, "grados"
            ))
