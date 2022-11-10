def calcula_media(M1,M2,M3):
    media = (M1+M2+M3)/3
    exame = media< 6.0
   
    if(media > 0.0 and media  <=4.0):
      print(f'Sua média final é ', media , 'Aluno REPROVADO')
    if(media >= 4.1 and media <= 6.0):
      print(f'Sua méida final é', media, 'Aluno de EXAME')
    if(media > 6.0):
      print(f'Sua média final é :', media, 'Aluno APROVADO')
    else:
       if(media > 10):
         print('Valor Inválido')
###### escrever abaixo

M1 = float(input('Digite a primeira nota: '))
M2 = float(input('Digite a segunda nota: '))
M3 = float(input('Digite a terceira nota: '))

calcula_media(M1, M2, M3)

if (media >=6.0):
    print (exame = float(input('Digite a nota do EXAME :')))
if (exame <6.0):
  print(f'Aluno APROVADO')
else:
    print(f'Aluno REPROVADO')
