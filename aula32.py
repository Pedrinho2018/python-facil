numero  = input('digite um numero: ')
if entrada.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'o numero {numero} é par')
    else:
        print(f'o numero {numero} é impar')
else:
    print('isso nao é um numero')   