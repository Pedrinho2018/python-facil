nome = input('digite seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome == 0:
    print('digite um nome valido')
elif tamanho_nome <= 4:
    print('seu nome é curto')
elif tamanho_nome <= 6:
    print('seu nome é normal')
else:
    print('seu nome é muito grande')
