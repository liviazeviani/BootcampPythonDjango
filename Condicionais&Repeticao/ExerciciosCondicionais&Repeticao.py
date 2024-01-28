"""
4. Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.
"""

notaDoAluno = int(input('Digite a nota - de 0 a 10: '))

if notaDoAluno >= 7:
    print('O aluno foi aprovado')
else:
    print('O aluno foi reprovado')


"""
10.Faça um programa que lê três números inteiros e os mostra em ordem crescente.
"""
#criando uma lista
listaDeNumeros = [] 

#solicitando números
numero1= int(input('Por favor digite um número inteiro: '))
numero2= int(input('Por favor digite outro número inteiro: '))
numero3= int(input('Por favor digite mais um número número inteiro: '))

#adicionando números na lista
listaDeNumeros.append(numero1)
listaDeNumeros.append(numero2)
listaDeNumeros.append(numero3)


#ordenando os números
listaDeNumeros.sort()

#mostrando a lista em ordem crescente
print(listaDeNumeros)


