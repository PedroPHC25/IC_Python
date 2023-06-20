def media2num(num1, num2):
    soma = num1 + num2
    media = soma/2

    return media

# print(media2num(1,5))

def media_args(*nums):
    soma = 0
    for i in nums:
        soma += i

    media = soma/len(nums)

    return media

# print(media_args(1, 2, 3, 4, 5, 6, 7, 8))

def media_kwargs(**dict):
    print(dict)

# media_kwargs(a=1, b=2, c=3)

def media_complexa(a, b, *lista, **dict):
    print(a, b, lista, dict)

# media_complexa(1, 2)

biblioteca = {}

def novo_livro(**dados):
    livro = {}
    
    for key, value in dados.items():
        try:
            dados[key] = value.title()
        except:
            pass
        livro[key] = value
    
    return livro
    
def adicionar_livro(*livros):
    for livro in livros:
        biblioteca[livro.get("Titulo")] = livro
    return biblioteca

livro1 = novo_livro(Titulo = "MLB", Autor = "jeremy zag", Editora = "ZAG studios", Ano = 2023)
livro2 = novo_livro(Titulo = "Cálculo", Autor = "stewart", Editora = "columbia", Edição = 9)


adicionar_livro(livro1, livro2)

# print(biblioteca)

def analise_estatistica(*numeros):
    lista_numeros = sorted(list(numeros))
    analise = {}

    media = sum(lista_numeros)/len(lista_numeros)

    lista_numeros = sorted(lista_numeros)

    if len(lista_numeros)%2 == 0:
        mediana = ((lista_numeros[int(len(lista_numeros)/2 - 1)] + lista_numeros[int(len(lista_numeros)/2)])/2)
    else:
        mediana = (lista_numeros[int(len(lista_numeros)/2)])

    moda = []
    ocorrencias = lista_numeros.count(lista_numeros[0])

    for numero in lista_numeros:
        if lista_numeros.count(numero) > ocorrencias:
            moda = []
            moda.append(numero)
            ocorrencias = lista_numeros.count(numero)
        elif lista_numeros.count(numero) == ocorrencias and numero not in moda:
            moda.append(numero)

    print(moda)

    analise["Valores"] = lista_numeros
    analise["Média"] = media
    analise["Mediana"] = mediana

    return analise

print(analise_estatistica(0, 1, 2, 3, 3, 4, 5))