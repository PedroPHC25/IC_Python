def funcaozinha1(num, soma = 1, mult = 2, exp = 3):
    result = num + soma
    result *= mult
    result **= exp
    return result
'''
print(funcaozinha1(5))

print(funcaozinha1(5, 5, 10)) # Parâmetros posicionais

print(funcaozinha1(5, 5, exp = 2)) # Parâmetros nominais

print(funcaozinha1(num = 5, soma = 5, exp = 2))

# print(funcaozinha1(num = 5, 5, 2)) # Não pode chamar parâmetros ordinalmente depois de nominalmente

print(funcaozinha1(5, exp = 5, soma = 2))
'''

def soma_arbitraria(*numeros):
    result = 0
    for i in numeros:
        result += i
    return result

# print(soma_arbitraria(1, 2, 3, 4, 5))

def soma2(*numeros, inicio = 0):
    for i in numeros:
        inicio += i
    return inicio

# print(soma2(1, 2, 3, 4, 5, inicio = -10))

def soma3(inicio = 0, *numeros):
    for i in numeros:
        inicio += i
    return inicio

# print(soma3(-10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


lista = [1, 2, 3, "EMAp", True]
tupla = (1, 2, 3, "EBAPE", False)

# print(type(lista), type(tupla))
# print(lista, tupla)

lista.remove(2)

# print(lista)

# del(tupla)
# print(tupla)

# print(tupla[0], tupla[4])
# print(tupla[0:3])