#   Listas e tuplas são formas de armazenar vários dados de uma vez só, diferente das
#variaveis tuplas e listas podem armazenar diversos dados com uma variedade de tipos 
#em uma só estrutura, eu acho que se chama estrutura composta o nome.
#   Existe algumas diferenças entre esses dois métodos de armazenamento de informação
#que que é importante saber antes de trabalhar com essas estruturas.
#   Tuplas são idedentificadas a partir do uso de '()' enquanto listas usam '[]',
#visualmente são distintas mas ambas podem até armazenar tuplas e listas dentro delas
#mesmas.
#   Tuplas são 'imutaveis' iso siginifica que se usar tuplas.append(1) resultará em um
#erro de imutabilidade, porque tuplas não podem sofrer mudanças, se você deseja mudar
#algum valor dentro de uma tuplas ou adicionar um novo valor, você deve primeiro criar
#uma nova tuplas e passar as modificações de forma conjunta a tupla anterior, e dessa forma
#você terá uma tuplas nova. Já as listas elas são mutáveis, podem ser modificadas com o possar
#do tempo sem resultar em erros.

#Listas
my_list = [1, 2.5, 'Marcos', True,['lista_2','*espaço',False],('tuplas_1', 2, 5)]
print(my_list)
#podemos printar partes específicas de uma lista ou tupla usando seus respectivos índices
print(my_list[0])
print(my_list[2])
print(my_list[3])
print(my_list[5])

#   Listas e tuplas possuem certas características que podem cer acessadas para retornar
#informaçõe sobre elas, seriam seus métodos.
lista_numeros = [1,12,66,4,14,66,9,0,66,11]
print(f'É possível printar o número de valores dentro de uma lista\nA lista {lista_numeros} tem {len(lista_numeros)} itens dentro')
print(f'A lista de números é composta de:\n{lista_numeros}\n usamos o comando .append(...) para adicioanr um novo valor a lista, no final dela')
lista_numeros.append(99)
print(f'adicionamos o valor 99 ao final da lista usando o .append(99) \n {lista_numeros}')
lista_numeros.insert(3,11)
print(f'Usamos o comando .insert(posição, item) para adicioanr um item em uma posição específica da lista\nAdicionando na posição 3 o item 11\n{lista_numeros}')
print(f'podemos encontrar a posição de um valor específico dentro de uma lista usando o .index(...)\n encontre o valor "11" e diga qual sua posição na lista')
print(f' Valor encontrado na posição [{lista_numeros.index(11)}] da lista')
print(f'Caso o valor não seja encontrado ele retorna um "ValurERRRO".\n exemplo: tente encontrar o valor "999"')
#print(f'O valor esta na posição {lista_numeros.index(999)}')
print('Usamos o .pop(...) e passamos no argumento o índice que queremos remover da lista')
lista_numeros.pop(2)
print(f'lista sem o valor presente na posição [3] -> {lista_numeros}')
print('Podemos usamo o .remove() e a lista vai retirar o primerio valor da lista que corresponde ao argumento')
print(lista_numeros)
print('Vamos remover o 66 com o .remove(66)')
lista_numeros.remove(66)
print(lista_numeros)
print('é posivel usar o .copy() para copiar todos os itens de uma lista para outra, e evitar o erro de listas gêmeas')
lista_numeros_copy = lista_numeros.copy()
print(f'primeira lista = {lista_numeros}\ncópia da lista = {lista_numeros_copy}')
print('podemos usar o comando .clear() e remover tudo da lista!')
lista_numeros.clear()
print(f'primeira lista = {lista_numeros}\ncópia da lista = {lista_numeros_copy}')

#Segunda parte do assunto!

#   Assim como podemos acessar um índice específico de uma lista através do lista[índice] podemos
#usar o ':' para acessar um conjunto de números a aprtir de um determinado range!
numeros = [1,2,3,4,5,6]

print(f'Nova lista de números : {numeros}\nAqui queremos acessar apenas o range de itens a aprtir do índice 1 até o 4º\n{numeros[1:4]}')

#   é importante salientar que quando dizemos que queremos que ele acesse o índice 1 até o índice 4,
#o sistema desconsidera o último valor, sendo assim printado apenas o 2, 3, 4 e desconsiderando o
#4 da lista.... não printando o item '5' que estaria no índice 4
print(f'printando o range de valores do 0 até o 3 \n{numeros[0:3]} desconsiderando o valor do índice 3')
#   É possível pintar todos os valores usando o índice vazio depois do ':'
print(f'Printando todos os valores depois do índice 3! e incluindo o últiumo valor\n{numeros[3:]}')
#   É interessante pensar que ele vai caminhando na lista até encontrar um avlor correspondente a 'null'
#na lista, ai ele "para de printar" na tela
print(f'Printando os valores da lista, com uma condição! nós podemos usar o 3º argumento depois do ":"')
print(f'Aqui ele vai pular de um em um \n{numeros[::2]}')
print(f'Aqui ele vau pular de dois em dois\n{numeros[::3]}')
print(f'Printando todos os valores em ordem reversa usando o -1, seria lista[::-1]\n{numeros[::-1]}')
#   Podemos usar essa característica dessa estrutura para copiar um determinado range para outra lista
print('Copiar os itens da lista de números para outra lista... só que a apartir de um índice espécífico')
numeros_copy = numeros[3:].copy()
print('Copiaremos a lista de números para outra lista usando o numeros[3:].copy()')
print(f'Lista de números original tem -> {numeros}')
print(f'A cópia da lista tem -> {numeros_copy}')

print(f'Podemos acessar ios índices de forma inversa numeros[-1] {numeros[-1]}')
print(f' numeros[-2] {numeros[-2]}')
print(f'numeros[:-1] {numeros[:-1]}')
print(f'Teste {numeros[::]}')
print('Aqui seria de trás para frente acessando todos os índices')
print(f'{numeros}\nTeste {numeros[::-1]}')
print('Aqui seria de trás para frente acessando 1 índice e pula outro índice')
print(f'{numeros}\nTeste {numeros[::-2]}')
print('Aqui seria de trás para frente acessando 1 índice e pula dois índices')
print(f'{numeros}\nTeste {numeros[::-3]}')
