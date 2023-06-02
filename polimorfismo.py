#Polimorfismo.

class Animal:
    def fazer_som(self):
        pass

class Leao(Animal):
    def fazer_som(self):
        print("O leão faz 'Aurrrrrrrr!'")

class Galinha(Animal):
    def fazer_som(self):
        print("O galinha faz 'Có có có có!'")

animais = [Leao(), Galinha()]

for animal in animais:
    animal.fazer_som()

#O comportamento polimórfico é evidenciado, pois cada animal faz um som diferente.