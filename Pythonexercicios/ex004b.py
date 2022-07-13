n = input(('Digite algo: '))
print('O tipo do valor {}  é {}: '.format(n, type(n)))
print('{} é um número? {} '.format(n, n.isnumeric()))
print('{} é só espaços? {}'.format(n, n.isspace()))
print('{} é alfabético? {}'.format(n, n.isalpha()))
print('{} é alfanumérico? {}'.format(n, n.isalnum()))








