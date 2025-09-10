# 6. Sistema de Votação (if/elif/else)
# Crie um programa que leia a idade de uma pessoa e informe se ela:
# não vota (menor que 16 anos)
# voto opcional (16 ou 17 anos, ou acima de 65 anos)
# voto obrigatório (de 18 a 65 anos)

numero = int(input("Digite sua idade: "))

if numero < 16:
    print("Impedido de votar")

elif numero < 18:
    print("Escolha de votar ou não")

elif numero <= 65:
    print("Voto obrigatório")

else:
    print("Escolha de votar ou não")
