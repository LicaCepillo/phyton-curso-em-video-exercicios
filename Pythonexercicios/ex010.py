# 'exercicio de conversor de moedas - Real em Dolar '#
moneyBR = float(input('Quanto dinheiro você tem na carteira ? R$ '))
dollar = moneyBR / 3.67
print('Com R$ {}, você pode comprar USD$ {:.2f}'.format(moneyBR, dollar))
