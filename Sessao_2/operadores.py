#   Sobre as operações matemáticas é fundamental entende-las, porque em programação nós usamos
#fundamentos matemáticos para compreender acesso de informações e manipulação de dados.
#dentr as mair diversas operações matemáticas vamos focar em entender seus respectivos 
#fundamentos e como esses mesmos se aplicam na programação.
print('Soma " + "- > 10 + 5 = ', 10 + 5)
#gosto da soma porque esse operador senver para somar números e também para concatenação de 
#strings, ams isso fica pra outro momento :D

print('subtração " - "- > 10 - 5 = ', 10 - 5)
print('divisão " / "- > 10 / 5 = ', 10 / 5)
print('multiplicação" * "- > 10 * 5 = ', 10 * 5,'\n')
print('existem outros operadores que podemos usar na programação:')
print('Exponenciação "**" - > 10 ** 2 = ',10**2) #é o mesmo que escrevermos 10^2 = 10 * 10 = 100
print('floor divide / ou divisão com arredondamento para baixo "//" = 10 //3 = ', 10//3)

#   É interessante esse floor divide porque ele aparentemente/visualmente apenas trunca o resutlado da 
#da divisão em um número sem virgura, e isso parece ser algo apenas visual... mas ele também converse 
#o tipo de dado, isso significa que o tipo resutlante de 10//3 não é um float e sim um int
print('\n10/3 resulta em ',10/3,'que seria do tipo: ',type(10/3))
print('mas se usarmos o "//" ou invés da barra comum "/"!')
print('10//3 resulta em ',10//3,'que seria do tipo: ',type(10//3))
print('interessante, não ? :D\n')

print('restante da divisão "%" 10 % 3 =',10 % 3, ) #muito utilizado para checar se o número é par ou ímpar

#   O professor do curso não se aprofundou muito sobre ordem de precedência numérica, mas isso é importante
#para programar, eu não vou falar muito porque eu vi isso no curso da Cisco Academy e no curso do Gustavo Guanabara
#mas é importante relembrar o básico...

print('5 + 5 * 2 = ', 5 + 5 * 2)
print('A ordem das operações muda conforme a organização de parênteses')
print('(5 + 5 ) * 2 = ', (5 + 5) * 2,'\n') #aqui o parênteses da prioridade a 5 + 5

print('True ou False são resultados lógicos que vem a partir de comparações ou chacagens de informações')
print(f'Ex:\n 10 > 2 = {10 > 2} ...  sim, 10 é maior que 2!')
print(f' 10 + 5 > 30 = {10 + 5 > 30} ...  não, 10 + 5 não é maior que 30!')
