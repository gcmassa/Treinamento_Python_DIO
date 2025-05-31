# Caso usando % em desusos
# %s para string
# %d para inteiro
# %f para float
# %x para hexadecimal
# %o para octal
# %e para exponencial
# %c para caractere
# %u para unicode
# %p para ponteiro
# %r para representação
# %a para representação ASCII
# %n para nova linha
# %t para tabulação
# %b para binário
# %g para notação científica
# %q para string formatada
# %m para moeda 

nome = 'Giancarlo'
idade = 43
profissao = 'programador'
linguagem = 'Python'

dados = {'nome': nome,
        'idade': idade,
        'profissao': profissao,
        'linguagem': linguagem}

print('Olá, me chamo %s! Eu tenho %d anos e sou %s. Você gosta de %s?' % (nome, idade, profissao, linguagem))

# metodo format

print('Olá, me chamo {}! Eu tenho {} anos e sou {}. Você gosta de {}?'.format(nome, idade, profissao, linguagem))

print('Olá, me chamo {0}! Eu tenho {1} anos e sou {2}. Você gosta de {3}?'.format(nome, idade, profissao, linguagem))

print('Olá, me chamo {nome}! Eu tenho {idade} anos e sou {profissao}. Você gosta de {linguagem}?'.format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem)) 

print('Olá, me chamo {nome}! Eu tenho {idade} anos e sou {profissao}. Você gosta de {linguagem}?'.format(**dados)) #dicionário

# metodo f-string

print(f'Olá, me chamo {nome}! Eu tenho {idade} anos e sou {profissao}. Você gosta de {linguagem}?')

# formatação usando f-string

PI = 3.14159265358979323846

print(f'O valor de PI é {PI:.2f}')  # 3.14

print(f'O valor de PI é {PI: 10.2f}')  # 3.14


# fatiamento de string

nome_completo = 'Giancarlo Massaccesi'

nome_completo[0] # G

print(nome_completo[0]) # G

nome_completo[:9]  # Giancarlo

print(nome_completo[:9]) # Giancarlo

nome_completo[10:16]  # Massaccesi

print(nome_completo[10:16]) # Massaccesi

nome_completo[10:16:2]  # Mscs

print(nome_completo[10:16:2]) # Mscs

nome_completo[:]  # Giancarlo Massaccesi

print(nome_completo[:]) # Giancarlo Massaccesi

nome_completo[::-1]  # isecacssaM olrCnaig

print(nome_completo[::-1]) # isecacssaM olrCnaig

#strings de multiplas linhas

texto = '''Olá, me chamo Giancarlo! Eu tenho 43 anos e sou programador. Você gosta de Python?'''

nome = 'Giancarlo'

mensagem = f'''Olá, me chamo {nome}! Eu tenho 43 anos e sou programador. Você gosta de Python?'''

print(mensagem) # Olá, me chamo Giancarlo! Eu tenho 43 anos e sou programador. Você gosta de Python?
