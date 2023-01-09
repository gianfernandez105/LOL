import math

acabar = False

def posacero (nombre,n):



print ("Escriu la sequència de naturals. Escriu 0 per acabar la llista:")


#cream una llista buida
llista=[]
#cream un token per acabar
acabar=False
while (not acabar):
    #agafam el nombre a calcular
    nombre int(input())
    if nombre == 0:
        acabar = True
    else:
       llista.append(nombre)
for x in llista:

print(llista)
