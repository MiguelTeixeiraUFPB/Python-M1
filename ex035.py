salario=float(input('digite seu salário: '))
if salario<=1250:
    aumento=(salario*15)/100
    print('o seu salário após o aumento é de {}'.format(salario+aumento))
else:
    aumento2=(salario*10)/100
     print('o seu salário após o aumento é de {}'.format(salario+aumento2))    
print()    