from definicao import Aluno

pedro = Aluno("Pedro Henrique Coterli", "Cîência de Dados e Inteligência Artificial", 42)
mariana = Aluno("Mariana Fernandes Rocha", "Cîência de Dados e Inteligência Artificial", 42)

# print(pedro.nome)
# print(mariana.matricula)
# print(pedro.cr)

# pedro.curso("Comunicação Digital")

pedro.curso = "Comunicação digital"

print(pedro.curso)

print(type(pedro))