lista = []
tupla = ()
conjunto = {}
dicionario = {}

dicionario = {"Aluno": "Almir", "Escola": "EMAp"}
dicionario = {"1": "Emap", "dois": "CdD", False: "Map", (1, 2, 3):[4, 5, 6]}

# Chave, valor e item (chave + valor)

dicionario[False] = "Direito"

# print(dicionario)

dicionario["Endereço"] = "Rua dos Bobos, nº 0"

# print(dicionario)

cartao = {}

cartao["Titular"] = "Marcelo Po"
cartao["Número"] = "1234 5678 1234 5678"
cartao["Data de vencimento"] = "31/02/2024"

novos_dados = dict()

novos_dados["CVV"] = 120

cartao.update(novos_dados)

# del cartao

cartao["Titular"] = "Marcelo Carvalhu Matheuz"

# cartao.clear()

# del cartao["CVV"]

# cartao.pop("CVV")

# print(cartao.pop("Chave inexistente", None))

cvv = cartao.pop("CVV")

# print(cvv)

cartao["Senha"] = 123456789
cartao["Ativo"] = True
cartao["Transacoes"] = [150, 20, 10, -580]

# print(cartao)

# for chave, valor in cartao.items():
#     print(chave, "->", valor)

# print(list(cartao.keys()))
# print(list(cartao.values()))

# for i in cartao["Transacoes"]:
#     print(i)

# print(cartao["Data de vencimento"])

# print(cartao.get("Senha"))
# print(cartao.get("Senha2", "Não achei!"))

novo_dict = dict()

novo_dict[None] = "Chave sem valor"

# print(novo_dict)

###########################################################

myset = {"maçã", "banana", "cereja"}

print(myset)

number_set = set(list(range(100)))

print(number_set)

lista_pares = [0, 2, 4, 8, 6, 4, 2, 0, 8, 6]

lista_sem_duplicatas = list(set(lista_pares))

print(lista_sem_duplicatas)

quiz = {}

print(type(quiz))

new_set = {"A", "E", "I", "O", "U"}
new_keys = {1, 2, 3, 4, 5}
# new_dict = dict(new_set)

new_dict = dict(zip(new_set, new_keys))

print(new_dict)

from sys import getsizeof

print(getsizeof(new_dict))