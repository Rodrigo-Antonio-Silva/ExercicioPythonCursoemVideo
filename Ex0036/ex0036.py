#coding utf-8
# exercício 36 provando empréstimo

valor_casa = float(input('Qual o valor da casa? '))
valor_salario = float(input('Qual o valor do salário do comprador? '))
duracao = int(input('Em quantos anos pretende quitar o imóvel? '))
duracao2 = duracao * 12

valor_prestacao = valor_casa / duracao2

if valor_prestacao > (valor_salario * 0.30):
    print('O valor R$ {:.0f} excede o limite de 30% do salário {}. Empréstimo negado!'.format(valor_prestacao, valor_salario * 0.30))
else:
    print('Parabéns! Empréstimo concedido com pagamentos mensais de R$ {:.2f} por {} anos.'.format(valor_prestacao, duracao))




