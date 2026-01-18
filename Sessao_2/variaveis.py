#   Variaveis sãoa  forma mais comum de armazenar dados em qualquer línguagem de programação
#   Variaveis recebem um nome que referência o endereço da memóroia no qual esse determinado
#dado está armazenado, isso significa que ao invés de escrevermos um códiggo hexadecimal que
#seria o endereço da mémoria... usamos um nome para nomear esse respectivo endereço :D
print('Variaveis!\n result = math opreratio\n print(result)')
print('Dessa forma o reusltado será printado na tela por meio da variavel :D')
print('nome = "mateus"\nprint(nome)')

#   No python nós não colocamos o tipo da variavel antes do nome dela, como fazemos em outras línuagens
#apenas colcoamos o nome dela e essa mesma receberá qualquer tipo de dado.

print('\n')
result = 10 + 5
print(result)
#   Result ainda detem o conteúdo da soma, isso significa que podemos utilziar esse respectivo
#dado para outros fins... inclusive na hora de armazenar outros dados dentro de outras variaveis
result2 = result / 2 
print(result2)
print('\n')

#   variaveis não podem conteer certos caacteres inicialmente como espaços, $, # ou % esses são
#caracteres especiais

print('Mais operações matemáticos na programação')
#   Em programação as vezes precisamos invrementar ou decrementar uma determinada variavel
#então a forma mais comum de escrever esse resultato é
numero = 1
print(f'numero = {numero}')
print('Pegamos o resultado de "numero" e adicionamos +1 usando o numero = numero + 1')
numero = numero + 1
print(numero)
print('Mas podemos usar o "+=" ao invés disso, e economizar código')
numero += 1
print(numero)
print('Isso também serve para quando você deseja decrementar um determinado valor dentro de uma variavel')
numero -= 1
print(f'numero = {numero}')
#podemos usar todos eles caso necessário '+=', '-=', '/=' e '*='