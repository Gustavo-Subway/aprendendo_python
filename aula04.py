#Quantos clientes você quer cadastrar

# NC = int(input("Quantos clientes você quer cadastrar?\n"))
# C= []

# v = [0 for i in range(NC)]

# for i in range(NC):
#     print(f"Digite o nome do cliente {i}")
#     C.insert(i, input("clientes: "))

# print(C)

# C.pop(2)
# print(C)


#Array multtdimensional

# C = [["José Carlos", "Vanessa", "Camila"], [35, 40, 10], ["Amarelo", "Verde", "Vermelho"]]

# print(C[0][1])
# print(C[1][1])
# print(C[2][1])


#Forma alternativa 

# NC = int(input("Quantos clientes você quer cadastrar?\n"))
# v = [0 for i in range(NC)]

# for i in range(NC):
#     print(f"Digite o nome do cliente {i}")
#     nome = input("Nome: ")
#     idade = int(input("Idade: "))
#     sexo = input(("Sexo: "))

#     v[i] = {
#          "nome": nome,
#          "idade": idade,
#          "sexo": sexo
#      }

# print("\nLista de Pessoas cadastradas")
# for pessoas in v:
#      print(pessoas)

# print(v[0])
# print(v[0]["nome"])

#Import

# from random import randint
# R = randint(0, 5)

# print(R)

#Adivinhe o sorteio

from random import randint
R = randint(1, 5)

N = int(input("Digite um numero entre 1 à 5\n"))

print(f"A maquina escolheu: {R}")

if (N == R):
    print("Wins")

else:
    print("Defeat")