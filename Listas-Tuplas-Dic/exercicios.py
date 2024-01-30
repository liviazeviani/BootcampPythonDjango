#exercício 1 - semana 3
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


#exercício 2 - semana 3
            
aluno = 1
medias = []
aprovados = 0

while aluno <= 5:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    print("-------------------------------")

    media = (nota1 + nota2 + nota3 + nota4) / 4

    medias.append(media)

    aluno +=1

for media in medias:
    if media >= 7:
        aprovados += 1


print(f"{aprovados} alunos obtiveram média maior ou igual a 7.0")

#exercício 3 - semana 3

carrinho = {}
carrinho['produto'] = 0
carrinho['arroz'] = 1
carrinho['feijão'] = 1
carrinho['leite'] = 3
carrinho['sal'] = 1
quantidade = sum(carrinho.values())
print(f'A quantidade de compras no seu carrinho é de {quantidade}')

#exercício 4 - semana 3

contatos = {} #criando dicionário
contatos['nome'] = 'telefone'

#exercício 5 - semana 3
#concatenação de tuplas

tupla_escola = ('lápis', 'caderno')
tupla_mercado = ('leite', 'pão')
print(tupla_escola + tupla_mercado)

#exercício 6 - semana 3
