#Ejercicio 1
m = int(input("Introduce a temperatura del día 1 en grados celsius: "))
n = int(input("Introduce a temperatura del día 2 en grados celsius: "))
o = int(input("Introduce a temperatura del día 3 en grados celsius: "))
p = int(input("Introduce a temperatura del día 4 en grados celsius: "))
q = int(input("Introduce a temperatura del día 5 en grados celsius: "))
r = int(input("Introduce a temperatura del día 6 en grados celsius: "))
s = int(input("Introduce a temperatura del día 7 en grados celsius: "))
l = (m,n,o,p,q,r,s)

#Ejercicio 2
media = sum(l) / 7
print("La temperatura media es de",media,"grados")

#Ejercicio 3
def calculoDias(contador):
    cantador = 0
    if valor>media:
        contador = contador + 1
    print("El total de días en los que la temperatura estubo por encima de la media fue de",contador)
print(calculoDias(contador))

#Ejercicio 4
for valor in l:
    if valor>media:
        if valor == m:
            print("El lunes la temperatura estubo por encima de la media ya que ese día hixo",m,"grados")
        elif valor == n:
            print("El martes la temperatura estubo por encima de la media ya que ese día fixo",n,"grados")
        elif valor == o:
            print("El miercoles la temperatura estubo por encima de la media ya que ese día fixo",o,"grados")
        elif valor == p:
            print("El jueves la temperatura estubo por encima de la media ya que ese día fixo",p,"grados")
        elif valor == q:
            print("El viernes la temperatura estubo por encima de la media ya que ese día fixo",q,"grados")
        elif valor == r:
            print("El sabado la temperatura estubo por encima de la media ya que ese día fixo",r,"grados")
        elif valor == s:
            print("El domingo la temperatura estubo por encima de la media ya que ese día fixo",s,"grados")