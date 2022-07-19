produto = float(input('Qual é o preço do produto: R$ '))
desconto = produto - (produto * 5/100)

print('O produto custa R$ {}, na promoção, com 5% de desconto, custa R$ {:.2f}'.format(produto, desconto))
