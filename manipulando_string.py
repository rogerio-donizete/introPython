curso = " curso de python  "
print(curso.upper())
print(curso.lower())
print(curso.title())
print(curso.strip())
print(curso.rstrip())
print(curso.lstrip())
print(curso.center(20, "#"))
print(".".join(curso))
print(curso.capitalize())

#Fatiar string

print(curso[1])
print(curso[:6])
print(curso[3:])
print(curso[3:6])
print(curso[1:5:2])
print(curso[:])
print(curso[::-1])

#string tripla

teste='mensagem'

mensagem=f'''Olá essa é uma {teste} de teste clear
para string tripla, taabém chamada de string multiplas'''
print(mensagem)




#interpolar variaves com %
nome= "Rogerio"
idade=46
profissao="desenvolvedor"
linguagem="Python"
pessoa={'age':46, 'name':'Rogério', 'profession':'profissao', 'linguagem':'Pytohn'}

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s. " % (nome, idade, profissao, linguagem))

#interpolar variaveis com o metodo format

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}. " .format(nome, idade, profissao, linguagem))

#interpolar variaveis com format numerado
print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {3} e estou matriculado no curso de {2}. " .format(nome, idade,linguagem , profissao))

#interpolar variaveis com format nomeado
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}. ".format(nome=nome, idade=idade,linguagem=linguagem , profissao=profissao))

#interpolar variaveis com format nomado por dicionario;
print("Olá, me chamo {name}. Eu tenho {age} anos de idade, trabalho como {profession} e estou matriculado no curso de {linguagem}. ".format(**pessoa))
 
 #interpolar variaveis com f-string
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")