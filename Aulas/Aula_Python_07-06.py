def palindromos(n):
    numeros = []
    i = 0
    while len(numeros) < n:
        i += 1
        string = str(i)
        digitos_diferentes = len(set(string))
        if digitos_diferentes > 1:
            inverso = string[::-1]
            if string == inverso:
                numeros.append(i)
    return numeros

# print(palindromos(1000))

def primo(n):
    primos = []
    for i in range(2, n):
        x = True
        for j in range(2, i):
            if i%j == 0:
                x = False
        if x == True:
            primos.append(i)
    i += 1
    return primos

# print(primo(100))

def palindromos_primos(n):
    numeros = []
    for i in primo(n):
        string = str(i)
        digitos_diferentes = len(set(string))
        if digitos_diferentes > 1:
            inverso = string[::-1]
            if string == inverso:
                numeros.append(i)
    return numeros

print(palindromos_primos(100000))