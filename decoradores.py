def meu_decorador(func):
    def wrapper():
        print("Antes de chamar a função.")
        
        print("Depois de chamar a função.")
        return wrapper
        func()  
    return wrapper

@meu_decorador
def minha_funcao():
    print("Esta é a minha função.")

minha_funcao()

class meu_decoradorDeclass:
    def __init__(self, func):
        self.func = func

    def __call__(self,) -> any:
        print("Antes de chamar a função com argumentos.")
        self.func()
        print("Depois de chamar a função com argumentos.")
        
@meu_decoradorDeclass
def minha_funcao():
    print("Esta é a minha função com argumentos.")