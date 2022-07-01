
import random
import math

cont = 0
run = True
b = []
b.append(0)
while (run):
    a= random.randint(0, 10)
    c = abs(b[cont]-a)
    b.append(c)
    cont += 1
    if (cont == 10):
        run = False
suma = 0

for i in b:
    suma += i

promedio = suma / cont

print (b)
print (promedio)
    


