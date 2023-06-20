### Conjuntos
'''
s = "abacaxi"

L = set(s)  

print(L)

L2 = {'c', 'x', 'i', 'b', 'a'}

print(L == L2)

print(L == {'c', 'a', 'b', 'x', 'i'})

L.add((1, 2, 3))

print(L)

L.add('a')

print(L)

print(L.union(L2))

print(L.intersection(L2))

print(L - L2)


d = dict(zip('abc', [1, 2, 3]))

print(d)

print(list(zip('casa', [1, 2, 3])))

print(d.keys())

d2 = dict(zip('peça', [1, 2, 3]))

print(d2.keys())

print(zip(range(2**345)), range(2**4))

print(list(zip(range(2**345), range(2**4))))
'''

### Assert

# assert 1 == 2

# assert []

assert [1]

def soma(*nums):
    for i in nums:
        try:
            assert isinstance(i, (int, float))
        except:
            print('Apenas números!')
    try:
        return sum(nums)
    except:
        pass


# print(soma(1, 2, 3, 4, 5))

# soma(1, 2, 'a')

def soma2(*nums):
    try:
        assert all([isinstance(i, (int, float)) for i in nums])
        return sum(nums)
    except AssertionError:
        print('Apenas números!')

# soma2(1, 2, 3, 'a')

# print(all([1, 2, 0]))

# print(soma2(1, 2, 3))
'''
x = input("Insira um número: ")

if '.' in x:
    valor = float(x)
else:
    valor = int(x)

print(valor*2)


try:
    a = float(input("Digite: "))
    print(f"Seu quadrado é {a**2}")
except:
    print("Isso não é um número!")
'''

class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som
        print(f"{self.nome} pronta!")
    def fala(self):
        print(self.som.upper() + "!")
    
vaca = Animal('vaca', 'Muuu')

vaca.fala()

cão = Animal('cão', 'Au Au')

cão.fala()