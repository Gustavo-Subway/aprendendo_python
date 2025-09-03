#Relenbrando 

# numero = int(input("Digite sua idade: "))

# if numero < 16:
#     print("Impedido de votar")

# elif numero < 18:
#     print("Escolha de votar ou não")

# elif numero <= 65:
#     print("Voto obrigatório")

# else:
#     print("Escolha de votar ou não")


#while

# numero = int(input("Digite um numero: "))

# while numero != 0:
#     print(f"Valor digitado é: {numero}")
#     numero = int(input("digite um numero: "))


#For

# for contador in range(11):
#     print("contador é: ", contador)


#Tabuada 


# n1 = int(input("Digite um numero para tabuada:\n"))

# for cont in range(1, 11):
#     r = n1 * cont 
#     print(f"{n1}\t *\t {cont}\t =\t {r}")


#Tabuada com While

n1 = 1

while n1 != 0:
    n1 = int(input("Digite um numero para tabuada, sendo 0 para parar:\n"))

    for cont in range(1, 11):
     r = n1 * cont 
     print(f"{n1}\t *\t {cont}\t =\t {r}")