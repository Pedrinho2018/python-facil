
numero_str = input('vou dobrar o numero que vc digitar :')

try:
    numero_float = float (numero_str)
    print(f'Float:',numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f})')
except:
    print('isso nâo é um numero')
