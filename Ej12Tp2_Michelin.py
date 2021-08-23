#Ejercicio 12 Tp 2 Michelin Brian

num = int(input("Ingrese el monto a retirar: "))

mil = num // 1000
num = num - (mil*1000)

quin = num // 500
num = num - (quin*500)
 
cien = num // 100
num = num - (cien*100)
 
cincu = num // 50
num = num - (cincu*50)
 
diez = num // 10
num = num - (diez*10)

print("Billetes de 1000 = ", mil)
print("Billetes de 500 = ", quin)
print("Billetes de 100 = ", cien)
print("Billetes de 50 = ", cincu)
print("Billetes de 10 = ", diez)

print("Saldo que no se pudo retirar: ", num)