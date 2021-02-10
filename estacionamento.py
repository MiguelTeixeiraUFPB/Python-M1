carros=int(input('qual a quantidade de carros que entrou?'))
qntvagas=42
qntvagasdisp=42-carros
faturamento=float(carros*1.75)
faturamentomax=float(qntvagas*1.75)
diferença=float(faturamentomax-faturamento)

print("""o número de carros que entrou é de: {} carros
O número de vagas no total é de: {} vagas
A quantidade de vagas disponíveis no momento é de: {} vagas
O faturamento atual é de: {}R$
O faturameneto total caso todas as vagas sejam preenchidas é de: {}R$
O estacionamento ainda pode faturar é de: {}""".format(carros,qntvagas,qntvagasdisp,faturamento,faturamentomax,diferença))

