num=int(input('digite um número: '))
resultado=num%2
if resultado==0:
    print('\033[1;34m esse número é par \033[m')
else:    
    print('\033[1;31messe número é impar\033[m')
print()    