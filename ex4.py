# 4. Faça um programa em Python que:
# Leia a largura e a altura de uma parede em metros.
# Calcule a área da parede.
# Calcule a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2 m².

l = int(input('digite a largura de uma parede: '))
a = int(input('digite a altura de uma parede: '))

r = l * a
t = r / 2

print('A area de sua parede é: ', r)
print(f'Para pinta-la sera necessario: {t} ')