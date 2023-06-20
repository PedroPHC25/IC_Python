# import sys

# def leitor(nome):
#     with open(nome) as f:
#         linhas = [tuple(l.strip().split('","') for l in f.readlines()[5:])]
#         print(linhas[:2])
#     lcab = len(linhas[0])
#     for n, l in enumerate(linhas):
#         try:
#             assert len(l) == lcab
#         except AssertionError:
#             print(n, len(l), l)

# if __name__ == "__main__":
#     leitor(nome = sys.argv[1])

