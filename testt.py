carne=float(8.5) #dividi o valor do kg por 2 para assim n precisar fazer a conversão de kg para grama
cerveja=float(1.80)
qntdpessoas=int(input('quantas pessoas vão ao churrasco?'))
preçocarne=qntdpessoas*carne
preçocerveja=qntdpessoas*(cerveja*6)
gasto=preçocarne+preçocerveja
print('o gasto para o número de {} pessoas é de {}'.format(qntdpessoas,gasto))

