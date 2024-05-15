# Exercícios: 

# 1 Imprima uma mensagem de boas-vindas na tela.


print('Seja bem vindo(a)!')


# 2 Declare uma variável booleana verdadeiro
# com o valor True e imprima seu tipo

booleana =  True 
print(type(booleana))


# 3 Imprima o resultado da multiplicação de dois 
# números decimais de sua escolha

print(1.2 * 3.4)



# 4 Imprima o resultado da divisão de dois números inteiros 
# de sua escolha.


print(4/2)

# 5 Imprima o resultado da subtração de dois números 
# inteiros de sua escolha

print(20-2)


# 6 Imprima o resultado da divisão inteira de dois números inteiros 
# de sua escolha.

print(10//2)


# 7 Imprima o resultado da multiplicação de dois
#  números decimais de sua escolha

print(3.5 * 2.9)

# 8 Declare uma variável numero e atribua um número inteiro. Em seguida, 
# imprima o dobro desse número


numero =  10
print(numero ** 2)


# 9 Crie uma calculadora de soma com as ferramentas que 
# vc já 
# conhece(Use apenas input, print e variavel)


numero1 =  float(input('Digite um número'))
numero2 =  float(input('Digite outro número'))

print(f'''
Resultado da soma: {numero1+numero2}
Resultado da subtração:{numero1-numero2}
Resultado da multiplicação:{numero1*numero2}
Resultado da divisão:{numero1//numero2}
'''
)



# 10 Crie um sistema de cadastro com as estruturas 
# que vc já 
# conhece(Use apenas input, print e variavel)
# nome, email, idade, altura


print('--------Formulario--------------')
nome  = input( 'Digite seu nome' )
idade = input('Digite sua idade')
email  =  input('Digite seu e-mail ')
altura = input('Digite sua altura')

print('olá', nome, 'sua idade e altura são', idade,'|' ,altura,'Contato:', email)


