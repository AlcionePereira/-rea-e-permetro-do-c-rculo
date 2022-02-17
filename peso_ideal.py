def peso_ideal():
    print('VAMOS SABER QUAL É SEU PESO IDEAL!')
    altura = float(input('Altura: '))
    sexo = int(input('''Qual é o seu sexo? 
    Digite 1 para feminino e 2 para masculino: '''))
    if sexo == 1:
         sexo = 'feminino'
         peso_legal =(62.1 * altura ) - 44.7
    elif sexo == 2:
        sexo = 'masculino'
        peso_legal = (72.7 * altura) - 58
        

    print(f'Você é do sexo {sexo}  seu peso ideal é {peso_legal:.2f}kg')

peso_ideal()
