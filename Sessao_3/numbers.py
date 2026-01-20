#   A diferença entre um float/double é o ponto de casas decimais, ambos são 'numbers'
#   Uma forma de descobri de qual tipo de dado estamos trabalhando é usar o 'type(...)'
print('Tipos de dados através do comando type()')
print(type(1))
print(type(1.5))

#   Podemos realizar operações e essas repectivas operações resultam em tipos de dados
#um exemplo seria somas um inteiro com um float ou dividir dois inteiros que resultam em um float
print(f'soma 1 + 1.5 = {1 + 1.5}, resulta em um tipo {type(1 + 1.5)}')
print(f'soma 10 / 5 = {10 / 5}, resulta em um tipo {type(10 / 5)}')

# É possível realizar conversões de números a partir de um método de conversão, exemplo:
print('Conversão de tipos de números para outros tipos :D')
print(f'2 é do tipo {type(2)} e convertemos ele usando float(2), que resutla em {float(2)} do tipo {type(float(2))}')
print(f'2.0 é do tipo {type(2.0)} e convertemos ele usando int(2.0), que resutla em {int(2.0)} do tipo {type(int(2.0))}')
print('\n arredondamento de dados usando round()')
print(f'5.9 usando o round(5.9) resulta em {round(5.9)}')
print(f'5.5 usando o round(5.5) resulta em {round(5.5)}')
print(f'5.3 usando o round(5.3) resulta em {round(5.3)}')