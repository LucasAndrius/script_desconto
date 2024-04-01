# Script de desconto pelo valor total da compra

Este é um programa em Python que calcula o desconto conforme o valor total da compra, seguindo as regras estabelecidas:

- Se o valor total da compra for menor que R$ 2500.00, o desconto será de 0%;
- Se o valor total da compra for igual ou maior que R$ 2500.00 e menor que R$ 6000.00, o desconto será de 4%;
- Se o valor total da compra for igual ou maior que R$ 6000.00 e menor que R$ 10000.00, o desconto será de 7%;
- Se o valor total da compra for igual ou maior que R$ 10000.00, o desconto será de 11%.

## Requisitos de Código:

1. Boas-vindas com o nome do programador.
2. Entrada do valor unitário e da quantidade do produto.
3. Cálculo do desconto conforme as condições especificadas.
4. Apresentação do valor total sem desconto e o valor total com desconto.
5. Utilização das estruturas if, elif e else.
6. Inclusão de comentários relevantes no código.

## Saída de Console:

1. Mensagem de boas-vindas com o nome do programador.
2. Pedido com desconto caso o valor total da compra seja acima de R$ 2500.00.

```python
# Print de boas vindas à loja
print('Bem-vindo à loja do Lucas Andrius de Oliveira')

# Variáveis para captura do valor unitário e quantidade
valorUnitario = float(input('Entre com o valor unitário do produto: '))
quantidade = int(input('Entre com a quantidade do produto: '))

# Variável responsável pelo cálculo do total da compra
totalCompra = valorUnitario * quantidade

# Verifica se o total é menor ou igual a 2500
if totalCompra <= 2500:
    print('Valor total da compra sem desconto: R${:.2f}'.format(totalCompra))

# Verifica se o total é menor que 6000
elif totalCompra < 6000:
    print('Valor total da compra sem desconto: R${:.2f}'.format(totalCompra))

    # Calcula o desconto de 4%
    desconto = totalCompra * 0.04
    print('Valor com desconto (4%): R${:.2f}'.format(totalCompra - desconto))

# Verifica se o total é menor que 10000
elif totalCompra < 10000:
    print('Valor total da compra sem desconto: R${:.2f}'.format(totalCompra))

    # Calcula o desconto de 7%
    desconto = totalCompra * 0.07
    print('Valor com desconto (7%): R${:.2f}'.format(totalCompra - desconto))

# Condição para totalCompra igual ou maior que 10000
else:
    print('Valor total da compra sem desconto: R${:.2f}'.format(totalCompra))

    # Calcula o desconto de 11%
    desconto = totalCompra * 0.11
    print('Valor com desconto (11%): R${:.2f}'.format(totalCompra - desconto))
```

Este programa solicita o valor unitário e a quantidade do produto, calcula o valor total da compra e aplica o desconto conforme as condições especificadas, apresentando o resultado na saída de console.
