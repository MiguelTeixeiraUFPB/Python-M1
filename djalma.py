disciplinas=int(input('quantidade de disciplinas por semana: '))
tempojudo=int(input('quantidade de tempo por aula de inglês em minutos: '))
tempoingles=int(input('quantidade de tempo por aula de judô em minutos: '))
ingles=tempoingles*2
minutoslivres=15*60
temposobra= minutoslivres-(ingles+tempojudo)
temposidciplinas= temposobra/disciplinas
print('o tempo por aula será de {:.1f} minutos por semana'.format(temposidciplinas))
