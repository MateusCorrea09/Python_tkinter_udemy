#   Inicialmente métodos são similares a funções, mas coma  diferença de que métodos
#são características pertencentes a objetos. Em programação nós podemos chamar uma função
#a qualquer momento no nosso código, já os métodos eles estão diretamente conectados aos
#objetos, e esses mesmos podem ser chamados a partir do uso de '.' no seu código
nome = 'Marcos Algusto'
print('Para colocar todas as letras em maíuscula usamos o ".upper()"')
print(nome.upper()) #Lembre-se de sempre usar o '()' para chamar um método
print('Para colcoar todas as letras em minúsculo usamos o ".lowe()"')
print(nome.lower())

#   Podemos usar os métodos de uma string para diversos fins, inclusive o de reorganizar uma
#entrada realizada pelo usuário
print('Usuario entrou com um nome "nome = "AmoRa ROXa" "\nPodemos usar o método ".title()" para deixar apenas\nem maíusculo a primeira letra do nome e sobrenome')
nome = 'AmoRa ROXa'
print(nome.title())

print('Podemos usar o .isalpha() para checar se uma determinada variavel possue apenas \ncaracteres do alfabeto')
print(nome)
print(f'nome é apenas alfabeto? = {nome.isalpha()}')
#isso deu 'False' porque em 'nome' tem um espaço entre as duas palavras :D e espaço não é um caractere
#do alfabeto! se removermos ele dara 'True' como resultado
nome = 'AmoRaROXa'.title()
print(nome)
print(f'nome é apenas alfabeto? = {nome.isalpha()}')

#   Importante lembrar que os métodos estão conectados aos objetos... e só usamos os métodos referentes
#os objetos do tipo string, existem outros tipos de objetos e esses mesmos possuem suas respectivas
#caracteríticas/métodos