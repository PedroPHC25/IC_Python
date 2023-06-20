# for i in range(10):
#     print(i)

# for i in range(-5, 10):
#     print(i)

# for i in range(-5, 10, 3):
#     print(i)

# range(start, stop, step)

# Geradores

gen = (i for i in range(10))

# print(gen)

d = {k:v for k, v in zip('casa', range(4))}

# print(d)

# for i in gen:
#     print(i)

def genf(n = 10):
    for i in range(n):
        yield i

gen = genf(10)

print(gen)
print(genf)

for i in gen:
    print(i)

def genf2(n = 10):
    x = 0
    for i in range(n):
        x = yield
        yield i + x

gen2 = genf2(10)

while True:
    gen2.send(10)
    next(gen2)