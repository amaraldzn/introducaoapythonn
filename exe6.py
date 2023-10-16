'''
Faça um programa que efetue a apresentação do valor da conversão em real (R$)
de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do
dólar e também a quantidade de dólares disponíveis com o usuário.
'''

cotacao = float(input('Informe o valor da cotação atual do dóllar: '))
quantidade = float(input('Informe a quantidade de doláres disponíveis para a conversão: '))

conversao = (cotacao*quantidade)

print('A sua quantidade disponível em real é:', conversao)

'''Alternativa que o CHATGPT deu

# Solicitar a cotação do dólar e a quantidade de dólares
cotacao = float(input('Informe o valor da cotação atual do dólar: '))
quantidade = float(input('Informe a quantidade de dólares disponíveis para a conversão: '))

# Calcular o valor em reais
conversao = cotacao * quantidade

# Exibir o resultado ao usuário
print(f'O valor convertido em reais é: R$ {conversao:.2f}')
'''
