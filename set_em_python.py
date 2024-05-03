#set são um acoleção de objetos e não possui valores repetidos. pode ser cirado com o construto set ou chaves
exemplos_lista_numero = set([1,2,3,1,3,5])
exemplos_string = set('abacaxi')
exemplo_tupla_carro = set(('palio', 'gol', 'celta', 'palio'))
print(exemplos_lista_numero)
print(exemplos_string)
print(exemplo_tupla_carro)

linguagens = {'python', 'python', 'java'}
print(linguagens)

#sets não possuem indeação e nem fatiamenteo, para acessar os valoes é necessário converter-los em uma lista.

numeros ={1, 2, 3, 4, 5, 6}
print(type(numeros))
numeros=list(numeros)
print(type(numeros))

#set aceitam iteração da mesma forma que lista (usando for e enumerate)

for numero in exemplos_lista_numero:
    print(numero)

for indice, carro in enumerate(exemplo_tupla_carro):
    print(f'{indice}: {carro}')

#metodos de set

conjunto_a = {1,2}
conjunto_b = {3,4}
conjunto_c = {2,3}
conjunto_d = conjunto_a.union(conjunto_b)
conjunto_e = conjunto_d.intersection(conjunto_c)
conjunto_f = conjunto_d.difference(conjunto_c)
conjunto_f2 = conjunto_c.difference(conjunto_d)
conjunto_f3 = conjunto_c.symmetric_difference(conjunto_d)

print(conjunto_d)
print(conjunto_e)
print(conjunto_f)
print(conjunto_f2)
print(conjunto_f3)

#issubset retorna verdadeio oou falso se é um subset
#issuperset retorna verdadeio oou falso se é um superset
#isdisjoint retorna verdadeiro oufalso de não ha intersecção.

#metodo add adicioona um elemento que ainda não exista no set, se esse elemento exisitir 'e ignorado.
#copy faz um copia do seu set
#clean limpa o seu set.
#discard elimian um elemento do set, se o valor não exist aele é ignorado
# pop, no set remove o primeiro valor.
#remove(valor) remover o valor passaado, mas retorna um erro.
#in retorna verdaderio ou falso se exite o valor no set.
