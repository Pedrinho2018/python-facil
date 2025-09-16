numero = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada do {numero}:")
print('-'*20)

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2} = {resultado}")    