# Importações
import re
import copy
import unicodedata

# Lista de produtos no estoque
estoque = [
    {"nome": "Arroz", "preco": 5.00, "quantidade": 100},
    {"nome": "Feijão", "preco": 6.50, "quantidade": 50},
    {"nome": "Macarrão", "preco": 3.80, "quantidade": 200},
    {"nome": "Óleo", "preco": 8.00, "quantidade": 75}
]

# Funções utilitárias
def remover_acentos(texto):
    # Normaliza o texto e remove os acentos
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto) 
        if unicodedata.category(c) != 'Mn'
    )

def normalizar_estoque(estoque_para_normalizar):
    # Normaliza os nomes dos produtos no estoque
    for produto in estoque_para_normalizar:
        produto['nome'] = remover_acentos(produto['nome']).lower()

# Funções principais
def exibir_produtos(estoque_para_exibir):
    # Exibe os produtos disponíveis no estoque
    print('Itens disponíveis para alteração:')
    for produto in estoque_para_exibir:
        print(f"Nome: {produto['nome']} | Preço: {produto['preco']} | Quantidade: {produto['quantidade']}")
        print()

def escolher_alteracao():
    # Solicita ao usuário o produto e o campo que deseja alterar
    produto_para_alterar = input('Qual produto deseja alterar? ')
    produto_para_alterar = re.sub(r'[^a-zA-Z0-9áéíóúãõçÂÊÎÔÛãõÁÉÍÓÚ]', '', produto_para_alterar)
    campo_para_alterar = input('O que deseja alterar? [N]ome [P]reço [Q]uantidade: ')
    campo_para_alterar = re.sub(r'[^a-zA-Z0-9áéíóúãõçÂÊÎÔÛãõÁÉÍÓÚ]', '', campo_para_alterar)
    return produto_para_alterar, campo_para_alterar

def alterar_valores(estoque_para_alterar, produto_para_alterar, campo_para_alterar):
    # Altera os valores do produto no estoque
    for produto in estoque_para_alterar:
        if produto_para_alterar == produto['nome']:
            if campo_para_alterar == 'n' or campo_para_alterar == 'nome':                
                novo_nome = input('Qual novo nome? ')
                produto['nome'] = novo_nome
            elif campo_para_alterar == 'p' or campo_para_alterar == 'preco':
                novo_preco = input('Digite o novo preço: ')
                produto['preco'] = float(novo_preco)
            elif campo_para_alterar == 'q' or campo_para_alterar == 'quantidade':
                nova_quantidade = input('Digite a nova quantidade: ')
                produto['quantidade'] = int(nova_quantidade)

def sincronizar_alteracoes(estoque_original, estoque_modificado):
    # Sincroniza as alterações feitas na lista secundária com a lista original
    for original, modificado in zip(estoque_original, estoque_modificado):
        original['nome'] = modificado['nome']
        original['preco'] = modificado['preco']
        original['quantidade'] = modificado['quantidade']

# Fluxo principal
estoque_normalizado = copy.deepcopy(estoque)        
normalizar_estoque(estoque_normalizado)

# Exibe os produtos disponíveis
exibir_produtos(estoque)

# Solicita as alterações ao usuário
continuar = True
while continuar:
    produto_para_alterar, campo_para_alterar = escolher_alteracao()
    produto_para_alterar = remover_acentos(produto_para_alterar).lower()

    # Aplica as alterações na lista secundária
    alterar_valores(estoque_normalizado, produto_para_alterar, campo_para_alterar)

    # Sincroniza as alterações com a lista original
    sincronizar_alteracoes(estoque, estoque_normalizado)

    # Pergunta se o usuário deseja continuar
    resposta = input('Deseja continuar? [S]im [N]ão: ')
    if resposta.lower() == 'n':
        continuar = False

# Exibe a lista original com os valores atualizados
print('Estoque atualizado:')
exibir_produtos(estoque)
