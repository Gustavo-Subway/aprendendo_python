#3. Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

a = int(input('Digite um valor em metros para converter em centimetros e milímetros: '))

b = a * 100
c = a * 1000

print('Seu valor em centimetros: ', b)
print('Seu valor em milimetros: ', c)