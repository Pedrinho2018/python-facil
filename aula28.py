name = input("digite seu nome:")
idade = input("digite sua idade:")
if name and idade:
    print(f'seu nome é {name}')
    print(f'seu nome invertido é {name[::-1]}')

    if ' ' in name:
        print('seu nome contem espaços')
    else:
        print('seu nome nao contem espaços')

    print(f'Seu nome tem {len(name)} letras')
    print(f'a primeira letra do seu nome é: {name[0]}')
    print(f'ultima letra do seu nome é: {name[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")
    exit()