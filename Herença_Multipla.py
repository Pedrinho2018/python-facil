class animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        raise NotImplementedError("Subclasses devem implementar este método")
    
class mamimfero(animal):
    def amamentar(self):
        return f"{self.nome} está amamentando seus filhotes."

class ave(animal):
    def voar(self):
        return f"{self.nome} está voando."

class morcego(mamimfero, ave):
    def fazer_som(self):
        return f"{self.nome} emite um som de morcego."
    
class cachorro(mamimfero):
    def fazer_som(self):
        return f"{self.nome} late."

morcego1 = morcego("Morceguinho")
print(morcego1.fazer_som())        # Saída: Morceguinho

morcego2 = morcego("Batinho")
print(morcego2.voar())  

print('nome do morcego:', morcego1.nome)
print("morcego emite som:", morcego1.fazer_som())
