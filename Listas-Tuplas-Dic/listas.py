# O que são listas

lista_frutas = [] 
lista_frutas.append('uva')
lista_frutas.append('banana')
#insirindo a lista a input do usuário
lista_frutas.append(input('Insira o nome da fruta que quer adicionar a lista: '))
#outra forma de adicionar input do usuário a lista
fruta = input('Por favor, digite qual fruta quer adicionar a lista: ')
lista_frutas.append(fruta)
print(lista_frutas)