#Formatação de mensagens

numero1 = int(input('Insira um número: '))
numero2 = int(input('Insira outro número: '))

soma = numero1 + numero2
divisao = numero1//numero2

print (f'A soma desses números é {soma}, já a divisão  é {divisao} ')

#Formatando corretamente

valor = 67.00
print(valor)
print(f'{valor:.2f}')

print('Olá {}, você tem {} anos de idade'.format('Lívia', 36))