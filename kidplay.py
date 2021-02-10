jogosv=int(input('digite a quantidade de jogos vendidos : '))
jogo=39.90
valorpjogo=2.50
comissão=jogosv*valorpjogo
porcentagem=(jogosv*39.90)*15/100
salario=porcentagem+comissão
print('o seu salário é de {}R$'.format(salario))