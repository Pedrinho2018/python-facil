compras =['arroz', 'feijão', 'macarrão' ]

print('------ Lista de Compras -----')
for item in compras:
    print(f'- {item}')

novo_item = input('Digite um novo item para adicionar à lista de compras: ')
compras.append(novo_item)

print('------ Lista de Compras Atualizada -----')
for item in compras:
    print(f'- {item}')

print(f'Temos {len(compras)} itens na lista de compras.')