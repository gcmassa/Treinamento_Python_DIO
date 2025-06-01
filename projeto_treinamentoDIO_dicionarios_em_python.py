# Treinamento DIO - dicionários em Python
# Dicionários em Python

pessoa = {'nome': 'Giancarlo', 'idade': 43} # Cria um dicionário com chaves e valores

pessoa = dict(nome='Giancarlo', idade=43) # Cria um dicionário com chaves e valores

pessoa['telefone'] = '3333-1234' # Adiciona um novo par chave-valor ao dicionário

dados = {'nome': 'Giancarlo', 'idade': 43, 'telefone': '3333-1234'} # Cria um dicionário com chaves e valores

dados['nome'] # Acessa o valor associado à chave 'nome'
dados['idade'] # Acessa o valor associado à chave 'idade'
dados['telefone'] # Acessa o valor associado à chave 'telefone'

dados['nome'] = 'Maria' # Atualiza o valor associado à chave 'nome'
dados['idade'] = 18 # Atualiza o valor associado à chave 'idade'
dados['telefone'] = '9988-1781' # Atualiza o valor associado à chave 'telefone'

print(dados) # Exibe o dicionário atualizado


contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '9999-9999'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '8888-8888'},
    'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '7777-7777'},
    'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '6666-6666'},
}

contatos['giovanna@gmail.com']['telefone'] # Acessa o telefone de Giovanna

teleofone = contatos['giovanna@gmail.com']['telefone'] # Acessa o telefone de Giovanna e armazena em uma variável
print(teleofone) # Exibe o telefone de Giovanna

for chave in contatos: # Percorre as chaves do dicionário contatos
    print(chave, contatos[chave]) # Exibe a chave e o valor associado a ela

print('=' * 100) # Linha de separação (comentada)

for chave, valor in contatos.items(): # Percorre as chaves e valores do dicionário contatos
    print(chave, valor) # Exibe a chave e o valor associado a ela


contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '9999-9999'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '8888-8888'},
    'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '7777-7777'},
    'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '6666-6666'},
}

contatos.clear() # Limpa todos os elementos do dicionário contatos
print(contatos) # Exibe o dicionário contatos após a limpeza, que estará vazio

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '9999-9999'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '8888-8888'},
    'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '7777-7777'},
    'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '6666-6666'},
}

copia = contatos.copy() # Cria uma cópia do dicionário contatos
copia['guilherme@gmail.com'] = {'nome': 'Gui'} # Atualiza o valor associado à chave '

contatos['guilherme@gmail.com'] # Acessa o valor associado à chave '
print(contatos['guilherme@gmail.com']) # Exibe o valor associado à chave '
copia['guilherme@gmail.com'] # Acessa o valor associado à chave '
print(copia['guilherme@gmail.com']) # Exibe o valor associado à chave '

dict.fromkeys(['nome', 'telefone']) # Cria um dicionário com chaves especificadas, mas sem valores
dict.fromkeys(['nome', 'telefone'], 'vazio') # Cria um dicionário com chaves especificadas e um valor padrão para todas as chaves

dados = dict.fromkeys(['nome', 'idade', 'telefone'], 'vazio') # Cria um dicionário com chaves especificadas e um valor padrão
print(dados) # Exibe o dicionário criado com chaves e valor padrão

#contatos['chave'] # Adiciona uma nova chave ao dicionário contatos

contatos.get('chave') # Acessa o valor associado à chave 'chave', retornando None se não existir
resultado = contatos.get('chave') # Acessa o valor associado à chave 'chave', armazenando em uma variável
print(resultado) # Exibe o resultado da busca pela chave 'chave'

contatos.get('chave', {}) # Acessa o valor associado à chave 'chave', retornando um dicionário vazio se não existir
resultado = contatos.get('chave', {}) # Acessa o valor associado à chave 'chave', armazenando em uma variável
print(resultado) # Exibe o resultado da busca pela chave 'chave'

contatos.get('guilherme@gmail.com', {}) # Acessa o valor associado à chave '
resultado = contatos.get('guilherme@gmail.com', {}) # Acessa o valor associado à chave '
print(resultado) # Exibe o resultado da busca pela chave '

contatos.items() # Retorna uma lista de tuplas contendo as chaves e valores do dicionário contatos
for chave, valor in contatos.items(): # Percorre as chaves e valores do dicionário contatos
    print(chave, valor) # Exibe a chave e o valor associado a ela

contatos.keys() # Retorna uma lista das chaves do dicionário contatos
for chave in contatos.keys(): # Percorre as chaves do dicionário contatos
    print(chave) # Exibe cada chave do dicionário

novo_contato = {'gian.massaccesi@gmail.com': {'nome': 'Giancarlo', 'telefone': '3333-1234'}} # Cria um novo dicionário com chaves e valores

resultado = novo_contato.pop('gian.massaccesi@gmail.com') # Remove a chave '
print(resultado) # Exibe o valor associado à chave removida

resultado = novo_contato.pop('gian.massaccesi@gmail.com', {}) # Remove a chave '
print(resultado) # Exibe o valor associado à chave removida, retornando um dicionário vazio se não existir

#novo_contato.popitem() # Remove e retorna o último par chave-valor do dicionário novo_contato
#novo_contato.popitem() # gera erro se o dicionário estiver vazio #KeyError: 'popitem(): dictionary is empty' # Gera um erro se o dicionário estiver vazio

novo_contato = {'nome': 'Giancarlo', 'telefone': '3333-1234'} # Cria um novo dicionário com chaves e valores	

novo_contato.setdefault('nome', 'Giovanna') # Retorna o valor associado à chave 'nome', ou define 'Giovanna' se não existir
print(novo_contato) # Exibe o dicionário após a operação setdefault
novo_contato.setdefault('idade', 28) # Retorna o valor associado à chave 'idade', ou define 28 se não existir
print(novo_contato) # Exibe o dicionário após a operação setdefault

novo_contato = {
    'gian.massaccesi@gmail.com': {'nome': 'Giancarlo', 'telefone': '3333-1234'}
 } # Cria um novo dicionário com chaves e valores

novo_contato.update({'gian.massaccesi@gmail.com': {'nome': 'Gian'}})
print(novo_contato) # Exibe o dicionário após a atualização

novo_contato.update({'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '8888-8888'}}) # Adiciona um novo par chave-valor ao dicionário
print(novo_contato) # Exibe o dicionário após a adição do novo par chave-valor


print('=' * 100) # Linha de separação

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '9999-9999'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '8888-8888'},
    'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '7777-7777'},
    'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '6666-6666'},
}

contatos.values() # Retorna uma lista dos valores do dicionário contatos
for valor in contatos.values(): # Percorre os valores do dicionário contatos
    print(valor) # Exibe cada valor do dicionário

# método in

'guilherme@gmail.com' in contatos # Verifica se a chave '
resultado = 'guilherme@gmail.com' in contatos
print(resultado) # Exibe o resultado da verificação se a chave '
'megui@gmail.com' in contatos # Verifica se a chave '
resultado = 'megui@gmail.com' in contatos
print(resultado) # Exibe o resultado da verificação se a chave '
'idade' in contatos['guilherme@gmail.com'] # Verifica se a chave 'idade' existe no dicionário associado à chave '
resultado = 'idade' in contatos['guilherme@gmail.com']
print(resultado) # Exibe o resultado da verificação se a chave 'idade' existe no dicionário associado à chave '
'telefone' in contatos['giovanna@gmail.com'] # Verifica se a chave 'telefone' existe no dicionário associado à chave '
resultado = 'telefone' in contatos['giovanna@gmail.com']
print(resultado) # Exibe o resultado da verificação se a chave 'telefone' existe no dicionário associado à chave '

# método del

del contatos['guilherme@gmail.com']['telefone'] # Remove a chave 'telefone' do dicionário associado à chave '
del contatos['chappie@gmail.com'] # Remove o dicionário associado à chave '

print(contatos) # Exibe o dicionário contatos após as remoções