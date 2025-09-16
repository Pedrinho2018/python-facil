print('====== Calculadora Simples ======')
print('1. Soma')
print('2. Subtração')
print('3. Multiplicação')       
print('4. Divisão')
print('5. Sair')    

opcao = input('Escolha uma opção (1-5): ')

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))

if opcao == '1':
    print('Resultado: ', a + b)
elif opcao == '2':
    print('Resultado: ', a - b) 
elif opcao == '3':
    print('Resultado: ', a * b)         
elif opcao == '4':  
    if b != 0:
        print('Resultado: ', a / b)
    else:
        print('Erro: Divisão por zero não é permitida.')   