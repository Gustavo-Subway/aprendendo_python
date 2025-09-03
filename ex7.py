# 7. Aprovação do Aluno (if/else)
# Faça um programa que leia a média final de um aluno e informe se ele está:
# Aprovado (média maior ou igual a 6)
# Reprovado (média menor que 6)

n1 = int(input("Nota 1:\n"))
n2 = int(input("Nota 2:\n"))

r = (n1 + n2) / 2

if r >= 6:
    print("Você está Aprovado!")

else:
    print("Você está Reprovado!")
