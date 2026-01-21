#   Pelo que eu entendi é um container similar ao dicionário com a diferença de que não
#há keys.
# sets podem ter seus conteúdos removidos e pode ter uma adição de um novo vonteúdo
# mas não podem ser atualizados.
#   sets não imutaveis
# 
test_set = {1,2,3,4}
print(test_set,type(test_set))
test_set.add(5)
print(test_set)
test_set.remove(2)
print(test_set) 
#test_set[0] não é possível acessar o índice de um set! resulta em um erro
#você pode chutar o primerio item em diante de um set
#print(test_set.pop(), ' / Aqui e chutei o 1')
#print(test_set, '/sem o 1 :D')

#   O que da pra fazer é usar uma conversão de dados apra converter o set em um outro tipo de dado
#que pode ser acessado por índices
new_struct = list(test_set)
print(new_struct,type(new_struct), f'O índice 1 tem o valor {new_struct[1]}')

