dias = int(input('Quantos dias você alugou o carro ?'))
km = float(input('Quantos Km você rodou? '))
total = (60*dias) + (0.15*km)
print('Você rodou {} km por {} dias, o valor a ser pago é R$ {}'.format(km, dias, total))
