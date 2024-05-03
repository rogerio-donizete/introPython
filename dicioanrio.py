pessoa = {'nome':'rogerio', 'idade':28}
pessoa1= dict(nome='rogerioD', idade=46)
pessoa['telefone']='3333-123'

# Dicionarop tão possuem chaves repetidas, e valores de chaves devem ser imutavel(passar tupla e não lista).
print(pessoa1 )

print(pessoa['nome'])
pessoa['nome']='lucas'
print(pessoa['nome'])

# dicioanrio aninhado

contatos = {"rogeriodds2003":{"nome":"rogerio", "telefone":"433-333"},
            "lucascruzsilvazruz":{"nome":"lucas", "telefone":"422-222"},
            "loreznodacruz2":{'nome': "lorenzo", "telefone":"533-222",},
            "deisedacruz":{"nome":"deise", "telefone":"411-123"}}

print(contatos['lucascruzsilvazruz']["telefone"])

#iteração em diconario com for:
for chave in contatos:
    print(chave, contatos[chave])

#iteração em diconario com metodos itens esse metodo retorna uma lista de tuplas.
for chave, valor in contatos.items():
    print(chave, valor)

#usando o in para verficar se a chaeve existente
print('lucascruzsilvazruz' in contatos)
print("danielpereira" in contatos)

#metodps
#clear limpa o dicionario
#copy - faz um segundo dicioanrio atraves da copia do priemiro.
#fromkeys -  cria novas chaves para o dicioanrio novo ou existente com um valor padrão ou com valor vazio
# get - acessa a chave do dicionario, mas precisa ser entre parenteses e não por colchetes, com cochetes funciona, mas se a chave não existir ele lança uma exceção.
# diconario.get9chave, {valor default})
# keys - informa as chaves de um dicioanrio.
#pop remove uma chave do dicionario e retorna o valor removido s epassado um valor padrão em caso de erro.
#pop.item - remover os itens de um dicioanrio na sequencio, se não hoiuve mais chaves retorna um erro.
#setdefault - passa a chave e um valor default se a chave exitir ele retornar o valor existente e não substituir, se a chave não exisitir ele cria a chave com o valor default.
#update, atualiza o diconario com um outro dcioanrio (chave:valor), se a chave exisitir ele atualiza todo o dicioanrio, se a chave não exisitir ele cria uma nova chave no dicioanro.
#values = retorna os valores se a chave.
#in  verifica se exite um achve no dicioabrio.
#del remove o objeto passado.
print(contatos.get('motor'))
