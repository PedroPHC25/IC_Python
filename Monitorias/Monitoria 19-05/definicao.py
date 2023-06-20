matriculas = [0]

class Aluno():

    def __init__(self, nome, curso, bolsa):
        self.__nome = nome
        self.__matricula = matriculas[-1] + 1
        matriculas.append(self.__matricula)
        self.__cr = None
        self.__curso = curso
        self.__notas = None
        self.__bolsista = bolsa

    @property

    def nome(self):
        print("Tudo certinho por aqui!")
        return self.__nome
    
    @property

    def matricula(self):
        return self.__matricula
    
    @property

    def cr(self):
        return self.__cr
    
    @property

    def curso(self):
        return self.__curso
    
    @property

    def bolsista(self):
        return self.__bolsista
    
    @property

    def notas(self):
        return self.__notas

    @curso.setter

    def curso(self, curso_novo):
        self.__curso = curso_novo