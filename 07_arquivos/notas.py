with open('notas.txt','w',encoding='utf-8') as f:
    f.write('primeira linha\n')
    f.write('segunda linha\n')

    print("arquivo 'notas.txt' criado com sucesso!")

with open('notas.txt','r',encoding='utf-8') as f:
    conteudo = f.read()
    print('Conteúdo do arquivo:')
    print(conteudo)