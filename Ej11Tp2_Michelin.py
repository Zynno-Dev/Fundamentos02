#Ejercicio 12 Tp 2 Michelin Brian

n=int(input("Ingrese el numero binario de 4 cifras"))

a = (n%10000 - n%1000) // 1000
b = (n%1000 - n%100) // 100
c = (n%100 - n%10) // 10 
d = (n%10)

print(a)
print(b)
print(c)
print(d)

r = ((a*2)**3) + ((b*2)**2) + ((c*2)**1) + ((d*2)**0)

print(r)