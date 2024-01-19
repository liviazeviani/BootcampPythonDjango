#1. Faça um Programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1*numero2
divisao = numero1/numero2

print(f'A soma desses dois números é {soma}')
print(f'A substração desses dois números é {subtracao}')
print(f'A multiplicação desses dois números é {multiplicacao}')
print(f'A divisão desses dois números é {divisao}')


#2. Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.

anoNascimento = int(input('Digite sua data de nascimento: '))
anoAtual = 2024

idade = anoAtual - anoNascimento

print(f'Sua idade é: {idade} anos')

#3. Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.

#4. Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.

#5. Escreva um programa que calcule o salário líquido. Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
#●Renda até R$1.903,98: isento de imposto de renda;
#●Renda entre R$1.903,99 e R$2. 826,65: alíquotade 7,5%;
#●Renda entre R$2.826,66 e R$3.751,05: alíquotade15%;
#●Renda entre R$3.751,06 e R$4.664,68: alíquotade22,5%;
#●Renda acima de R$4.664,68: alíquotamáximade27,5%.

#6. Escreva ump rograma que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião,carro e ônibus. Levando em consideração: ●avião= 600km/h ●carro= 100km/h● ônibus= 80km/h

#7. Solicite ao usuário o peso em kg e a altura e metros. Calcule e imprima o Índice de Massa Corporal(IMC) usando a fórmula: IMC=peso/(alturaxaltura).


# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas nomês. Calcule e mostre o total do seu salário no referido mês.

#9. Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.

#10. Faça um Programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas. Exemplos de variáveis: nome, idade, lugar, profissão.... Exemplo de retorno: Olá Maria,prazer te conhecer. Sou de São Paulo também e estou migrando de área. Lembrando que para o retorno vamos usar print com as variáveis criadas e este texto é somente um exemplo, utilizem a criatividade

nome = input('Por favor, digite seu nome: ')
idade = input('Por favor, digite sua idade: ')
estado = input('Qual o estado que você reside: ')
email = 'brazil@pyladies.com'

print (f'Olá {nome}, você está com {idade} e reside no estado de {estado}. Envie um e-mail para {email} e saiba mais informações sobre o grupo PyLadies, um grupo com o propósito de ajudar mais e mais mulheres a se tornarem participantes ativas e líderes na comunidade open source Python' )