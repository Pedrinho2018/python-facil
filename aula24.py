# operadores in e not in
# strings sao iteraveis
# 0 1 2 3 4 5
# o t a v i o
#-5 -4 -3 -2 -1
#nome = 'otavio'
#print(nome[2])  
#print(nome[-4]) 
#print('a' in nome) 
#print('z' in nome)
#print(10*'-')
#print('vio' not in nome)
#print('zero' not in nome)
nome = input("Digite seu nome: ")
encontrar = input("Digite uma letra para encontrar no seu nome: ")
if encontrar in nome:
    print(f'A letra "{encontrar}" foi encontrada no seu nome')
else:
    print(f'A letra "{encontrar}" não foi encontrada no seu nome')
    