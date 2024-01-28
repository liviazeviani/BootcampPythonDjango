print('Resposta as seguintes perguntas apenas com SIM ou NÃO')
resposta1 = input('Telefonou para a vítima? ')
resposta2 = input('Esteve no local do crime? ')
resposta3 = input('Mora perto da vítima? ')
resposta4 = input('Devia para a vítima? ')
resposta5 = input('Já trabalhou com a vítima? ')

respostas = []

respostas.append(resposta1)
respostas.append(resposta2)
respostas.append(resposta3)
respostas.append(resposta4)
respostas.append(resposta5)


    

classifica = respostas.count('SIM')
if classifica <= 1:
            print('Classificação: Inocente')
elif classifica <= 2:
            print('Classificação: Inocente')
elif classifica <= 3:
            print('Classificação: Suspeito')
elif classifica <= 4:
            print('Classificação: Cúmplice')
else:
            print('Classificação: Assassino')