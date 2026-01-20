#   Sobre a criação de strings podemos usar tanto aspas simples '' quando a conjunta "", pelo
#que o professor falou também é possível usar o `` assim como no JS :D
#   String spossuem diversos métodos que podem seru utilizados para realizar varios tratamentos
#de entradas realizadas pelo usuário, além do básico que seria a concatenação de elementos usando '+'
#   Em python usamnos o \n para sinalizar que há uma quebra de linha em uma string
var_1 = 'linha 1:... \nlinha 2:...'
print(var_1)
#   Em python o /t é como se fosse um tab
print('\n')
var_2 = 'linha 1:... \tlinha 2:...'
print(var_2)
#   Também podemos usar as aspas de comentários para comunicar multiplas linhas em ums string
print('\n')
var_3 = '''Comentário
linha1:...
linha2:...'''
print(var_3)

#   Em python podemos realizar concatenação de string usando o '+'
palavra_1 = 'Olá'
palavra_2 = 'Mundo!'
print(palavra_1+palavra_2) #Elas serão juntadas como se fossem uma palavra apenas, sem espaço
#   Em python também podemos realizar multiplicação de strings, quando queremos repeti-las um
#de vezes em sequência

print('\nOlá mundo!' * 10)
print('\nPodemos colcoar valores dentro de strings')
nome = 'bob'
idade = 50
descriocao = '{} tem {} anos'.format(nome,idade)
print(descriocao)
#   Ou podemos usar o 'f' antes das aspas, é mais sofisticado
nome = 'Alexandre'
idade = 33
descriocao = f'{nome} tem {idade} anos'
print(descriocao)
#   As duas formas resultam no mesmo... resultado :D

#Exercício: crie uma f-string que tenha seu nome e idade separado por espaços e que use oq vc aprendeu
nome = 'Mateus'
idade = 25
print(f'Olá meu nome é {nome} tenho {idade} anos, e gosto de estudar Python! :D')