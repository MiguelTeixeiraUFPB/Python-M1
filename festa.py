qntbrigadeiros=int(input('digite a quantidade de brigadeiros que deseja comprar: '))
qntcajuzinho=int(input('digite aquantidade de cajúzinhos q deseja comprar: '))
qntdcrianças=int(input('digite a quantidade de crianças: '))
brigadeiro=0.90
medideconsumo=(qntcajuzinho+qntbrigadeiros)//qntdcrianças
cajuzinho=0.70
precobriga=qntbrigadeiros*brigadeiro
precocaju=qntcajuzinho*cajuzinho
total=precobriga+precocaju
print('o preço final é de {} e a média de docinhos q cada criança consumirá é de {}'.format(total,medideconsumo))

