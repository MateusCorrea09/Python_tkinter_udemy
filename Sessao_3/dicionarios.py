#   Dicionários ainda são containers assim como tuplas e listas, mas tem suas peculiaridades
#em um dicionário nós temos alguns nomes de suas propriedades, inicialmente são elas 'key' e 'value'
#'key' seria o índice desse dicionário e 'value' seria o conteúdo desse índice (assim como tuplas
# e listas). 
#   O python é bem flexível em relação aos tipos de dados, isso signific que key e value podem ser
# de qualquer tipo de dado.

test_dict = {'A': 123, 'B': [1,2,3]}
print(test_dict)
#   Não coloque um novo item no dicionário com a mesma 'key'! pois o python  irá sobreescrever o
#valor por cima
test_dict = {'A': 123, 'B': [1,2,3], 'A': 'Another value'}
print(test_dict)
test_dict = {'A': 123, 'B': [1,2,3]}

#   Através de alguns métodos podemos acessar ou manipular os dados dentro de um dicionário
print('*Pritando todos os "value" dentro do dicionário: ',test_dict.values(),sep='\n')
print('*Pritando todos os "key" dentro do dicionário: ',test_dict.keys(),sep='\n')
print('*Pritando todos os "items" dentro do dicionário: ',test_dict.items(),sep='\n')
#   Interessante visualizar que o .items() retorna uma lista com tuplas... e essas tuplas armazenam
#os dados da seguinte forma (key, value) :D
print('\nConvertendo dicionários!\n')
#   Percebá como é a conversão de dados!!!
print(list(test_dict))
print(tuple(test_dict))
print(str(test_dict))
print('Usando o ".items()" para separar tudo e converter da forma correta')
print(list(test_dict.items()))
print(tuple(test_dict.items())) #Aqui virou numa tupla dentro de uma tupla de tuplas :D
print('\n Acessando os conteúdos dentro de um dicionário')
print(test_dict['A'])
print(test_dict.get('B'))
#   A diferença entre os dois está no retorno de cada um, se vc usar o 'test_dict['X']' e 'X' não
#Existir ele vai retornar um erro, que consequêntemente isá crachar seu programa, mas se você usar
#o get o retorno de 'X' será 'none' caso 'X' não existir :D mais eficiente 

#EXERCÍCIO adicione um novo valo ao dicionário
#OBS: eu fui na documentação achar algumas coisa sobre '.update' ou algum método de 'insert()' rsrsrs
#ai lembrei que é só adicionar uma key que ainda não exista e um value para ela, isso tudo entre '[]'
#ai ele adiciona o novo conteúdo dentro do cidionário 
test_dict['novo'] = 42
print(test_dict)
#   Para atualizar eu só preciso pegar o key e dizer qual o novo value dele
test_dict['novo'] = 11
print(test_dict)
#   Vendo a resolução do professor eu vi ele usar o .update() e agora eu entendi como usar esse
#metodo, eu vi que ele precisou passar entre '{}', porque é um dicionário, o novo conteúdo
test_dict.update({'Another_Value': (1,2,3,4,5)})
print(test_dict)
