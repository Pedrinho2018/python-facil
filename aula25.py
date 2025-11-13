'''
intepolação basica de strings 
s - string  
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
'''
nome='luiz'
preco = 1000.958976
variavel = '%s, o preco total é R$ %.2f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d é %08X' % (1500, 1500))