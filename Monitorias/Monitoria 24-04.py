# Tipos de variáveis: bool, int, float e string
# Condicionais: if, elif e else
# Laços/loops/estruturas de repetição: while e for

for i in range(10):
    print(i)

alfabeto = ["A", "B", "C", "D"]

# ENUMERATE

for elemento in enumerate(alfabeto):
    print(elemento)

grego = ["alpha", "beta", "gamma", "phi", "delta"]

# ZIP

for letra, grega in zip(alfabeto, grego):
    print(letra, grega)

# SLICE

# pixel = [R, G, B]

verde = [1, 2, 3]

print("canal vermelho:", verde[0])

print("Canais vermelho e azul:", verde[0], "e", verde[2])

print("Canais vermelho e verde:", verde[0:2])

print("Canais vermelho, verde e azul:", verde[0:3])

print("Canais verde e azul:", verde[1:3])

print(verde[1:])

print(verde[:2])

# SLICE: STEP

print(verde[::2])

inteiros = range(1, 100, 2)

for elemento in inteiros:
    print(elemento)

lista = ["A", "B", "C", "D", "E", "F"]

for valor in lista[::2]:
    print(valor)

for index in range(0, len(lista), 2):
    print(index)

for index in range(0, len(lista), 2):
    print(lista[index])

# ÍNDICE NEGATIVO

print(lista[-3])

print(lista[-1:])

print(lista[-1::-1])

# PRINT DE LISTAS

for elemento in lista:
    print(elemento, end=', ')

print(', '.join(lista))

# F STRINGS

idade = 16

print("Tenho 15 anos")

print("Tenho", idade, "anos")

print(f"Tenho {idade} anos")

print("#############################")

# PROCURA DE ITENS: IN

alunos = ["Almir", "Adalberto", "Ademar", "Oracio", "Edwaldo", "Itamar"]

for elemento in alunos:
    if elemento == "Beatriz":
        print("ACHEI!")
        break

if "Itamar" in alunos:
    print("ACHEI!")
else:
    print("Não achei...")

if ["Almir", "Itamar"] in alunos:
    print("ACHEI!")
else:
    print("Não achei...")

alunos.append(["Almir", "Itamar"])

print(alunos)

if ["Almir", "Itamar"] in alunos:
    print("ACHEI!")
else:
    print("Não achei...")

if "Adalberto" and "Itamar" in alunos:
    print("ACHEI!")
else:
    print("Não achei...")

print("#############################")

# OPERAÇÃO INPLACE (SHALLOW COPY / CÓPIA SUPERFICIAL)

liste = [1, 8, 6, 4, 3, 5, 0, 2]

liste.sort()

print(liste)

# OPERAÇÃO NOT INPLACE (DEEP COPY / CÓPIA PROFUNDA)

listi = [1, 8, 6, 4, 3, 5, 0, 2]

listiordenada = sorted(listi)

print(listi)
print(listiordenada)

listicp = listi.copy()
print(id(listi), id(listicp))

listi.append(11)
print(listi, listicp)

listicp2 = listi
print(id(listi), id(listicp2))

listi.append(11)
print(listi, listicp2)