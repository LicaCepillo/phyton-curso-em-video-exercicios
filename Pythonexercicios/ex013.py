salario = float(input('Qual é o salário do funcionário? R$ '))
novosal = salario + (salario * 15 / 100)
print('O salário do funcionário era de R$ {:.2f}, depois do aumento de 15% passou a ser R${:.2f}'.format(salario,
                                                                                                         novosal))
