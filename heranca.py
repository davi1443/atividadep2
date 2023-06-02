#Herança

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Olá, eu me chamo {self.nome}.")

class Estudante(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)
        self.curso = curso

    def apresentar(self):
        super().apresentar()
        print(f"Eu estudo {self.curso}.")

estudante = Estudante("Davi", "Engenharia")
estudante.apresentar()

# A classe Estudante herda da classe Pessoa e adiciona um atributo curso e uma implementação diferente do método apresentar()