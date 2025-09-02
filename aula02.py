#Operadores

# n1 = int(input('Digite um numero inteiro: '))
# n2 = int(input('digite um segundo numero: '))

# soma = n1 + n2
# divisão = n1 / n2
# multiplicacao = n1 * n2
# subtracao = n1 - n2
# sobra = n1 % n2
# divisaoInteira = n1 // n2
# potenciacao = n1 ** n2
# raiz = pow(n1, 0,5)

# print('A Soma é: ', soma)
# print('A Divisão é: ', divisão)
# print('A Multiplicacao é: ', multiplicacao)
# print('A subtracao é: ', subtracao)
# print('A sobra é: ', sobra)
# print('A divisao Inteira é: ', divisaoInteira)
# print('A Potenciacao é: ', potenciacao)
# print('A raiz é: ', raiz)

#Funções condicionais

print('=======================')
print('Sistema de horas')
print('=======================')

h = int(input('Digite um Horario: '))

if h < 12:
    print('Bom Dia!')

elif h < 18:
    print('Boa Tarde!')

else:
    print('Boa Noite!')