'''
Las Tuplas son Inmutables
'''

tupla = ("uno", "dos", "tres")
print(tupla)

tuplaVariosDatos = (12, True, 23.5, "El gato", 12+2)
print(tuplaVariosDatos)

tupplasConTuplas = (1,2,3,4,(1,2,3))
print(tupplasConTuplas)
print(tuplaVariosDatos[3])
print(tuplaVariosDatos[-2])
print(tuplaVariosDatos[0:2])

a,b,c = tupla

print(a)
print(b)
print(c)


tuplaNueva = tupla+tuplaVariosDatos
print(tuplaNueva)