#   As funções são comandos especiais de uma linguagem de programação!
#   Em python temos algumas funções que já utilizamos no nosso curso, como o print(),
#print() é uma função que por meio dos parênteses espera algum 'Argumento' que seria o
#oq será printado na tela
print('Ola mundo!') #aqui chamamos a função 'print()' e passamos uma string como parâmetro
#   Aqui eu pedi para função 'print()' printar o tipo de retorno que um print dá
print(type(print('olá mundo!')))
#Interessante ver que ele acessou o 'olá mundo' primeiro antes de retornar o tipo de dados que
#o print retorna... é como se ele fosse primeiro no núcleo e depois para fora :D
#   Em uma função podemos ter varios argumentos, e eles podem ser separados por ','
print('Olá', 'mundo!') # aqui a ',' atua não só como separador de argumentos mas também da espaço
                        #entre eles
print('Olá','mundo',sep=' *Espaço* ')
#   Na função print podemos também acessar esses respectivos atributos para modificar seus compartamentos
#se você passar o mouse em cima da escrita 'print' você consegue ter acesso a documentação que diz
#oq a função faz, seus respectivos argumentos e uma breve explicação sobre.
print(f'A função "max()" retorna o maior numero dentre um numero x\nde argumentos que foram passados (no caso dois ou mais :D)\n{max(2,11,45,12,6,1,0,10,-11,4)} foi o maior número apssado')
print('\n')
#   Podemos criar nossas próprias funções por meio do comando 'def'
def soma(n1,n2):
    return n1 + n2
print(soma(2,2))
print(soma(3,3))
#Eu acho que o professor vai falar mais sobre isso ao decorrer do curso, então não vou correr com isso
#:D
def carinha():
    print(':D')
carinha()