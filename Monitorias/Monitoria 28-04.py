### DEVER DE CASA: LIST COMPREHENSION ###
# W3SCHOOLS


### INPUT ###

# a = float(input('Digite um número: '))
# quadrado = a**2
# print(f"Seu quadrado é {quadrado}!")

# a = int(float(input('Digite um número: ')))
# print(f"Seu float convertido em inteiro é {a}!")


### FUNÇÕES ###

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

# for num in lista1:
#     print(num**2)

# for num in lista2:
#     print(num**2)

def imprimir_quadrado(lista):
    for num in lista:
        print(num**2)

# imprimir_quadrado(lista1)
# imprimir_quadrado(lista2)

def imprime_oi():
    print("Oi, galera!")

# imprime_oi()

### FUNÇÕES COM VÁRIOS ARGUMENTOS ###

def media_3(num1, num2, num3):
    soma = num1 + num2 + num3
    media = soma/3
    print(f"Média = {media}")

# media_3(5, 10, 15)

def media_que_retorna(num1, num2, num3):
    soma = num1 + num2 + num3
    media = soma/3
    return media

average = media_que_retorna(5, 10, 15)

# print(average)

# print(type(average))

def negativo(num1, num2, num3):
    a = num1 * -1
    b = num2 * -1
    c = num3 * -1
    return a, b, c

neg = negativo(42, 666, 69)

# print(neg)

x, y, z = negativo(42, 666, 69)

# print(x)
# print(y)
# print(z)

def potencia(base, expoente = 2):
    return base**expoente

# print(potencia(10))
# print(potencia(10, 10))

