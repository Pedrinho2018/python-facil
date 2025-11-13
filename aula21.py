#operadores logicos e de comparação
# and (e), or (ou), not (não)
#and = todas as condições devem ser verdadeiras
#se quaquer valor for considerado falso, o resultado será falso
#se todos os valores forem verdadeiros, o resultado será verdadeiro
# print(True and True and True) #True
# print(True and False and True) #False
# print(1==1 and 2==2) #True
# print(1==1 and 2!=2) #False
# print('Pedro'=='Pedro' and 'Python'=='Python') #True
# print('Pedro'=='Pedro' and 'Python'=='python') #False
# print(10>5 and 5<10 and 10==10) #True
# print(10>5 and 5>10 and 10==10) #False       


"""entrada = input("[e]ntrar [s]air: ")
senha = input("Senha: ").strip()
senha_permitida = '1234'

if entrada == 'e' and senha == senha_permitida:
    print("Você entrou no sistema")

else:
print("Entrada inválida")  """

#avaliaçao de curto circuito
senha = input("Senha: ") or 'Sem senha'
print(senha)