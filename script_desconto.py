#Print de boas vindas a loja
print('Bem-vindo a loja do Lucas Andrius de Oliveira')

#Váriaveis de captura de valor unitário e quantidade
valorUnitario = int(input('Entre com o valor unitário do produto: '))
quantidade = int(input('Entre com a quantidade do produto: '))

#Variável responável pela soma do total
totalCompra = valorUnitario * quantidade

#Verifica se o total é menor ou igual a 2500
if (totalCompra <= 2500):
    print('Valor total da compra foi: R${}'.format(totalCompra))

#Verifica se o total é menor que 6000
elif (totalCompra < 6000):
    print('O Valor sem desconto foi: R${}'.format(totalCompra))

    #Variável que calcula o desconto de 4%
    desconto = totalCompra * (4 / 100)
    print('O valor com desconto foi: R${}'.format(totalCompra - desconto))

#Verifica se o total é menor que 10000
elif (totalCompra < 10000):
    print('O Valor sem desconto foi: R${}'.format(totalCompra))

    #Variável que calcula o desconto de 7%
    desconto = totalCompra * (7 / 100)
    print('O valor com desconto foi: R${}'.format(totalCompra - desconto))

#Condição para totalCompra igual ou maior que 10000
else:
    print('O Valor sem desconto foi: R${}'.format(totalCompra))

    #Variável que calcula o desconto de 11%
    desconto = totalCompra * (11 / 100)
    print('O valor com desconto foi: R${}'.format(totalCompra - desconto))