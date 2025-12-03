pessoa = {'nome': 'pedro', 'idade': 25, 'cidade': 'São Paulo'}

print(pessoa['nome'])  # Acessando valor pela chave 'nome'
print(pessoa.get('idade'))  # Acessando valor pela chave 'idade' usando get()
print(pessoa.keys())  # Obtendo todas as chaves do dicionário
print(pessoa.values())  # Obtendo todos os valores do dicionário
print(pessoa.items())  # Obtendo todos os pares chave-valor do dicionário
print(len(pessoa))  # Obtendo o número de itens no dicionário


chave = 'cidade'
if chave in pessoa:
    print(f"A chave '{chave}' existe no dicionário.")