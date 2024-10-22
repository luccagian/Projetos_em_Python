#sistema para analise de dados dado um aquivo csv
'------------------------------------------------'

#abrindo o aquivo do excel

dataset = open('emack.csv','r')

#criando uma lista de listas com todos os itens do arquivo e separando a matriz por ',' e '[]'

lista =[]

for linha in dataset:
    x = linha.split(',')
    lista.append(x)

#criando um dicionario a partir de uma lista a chave deste dicionaro é o indice i da linha 0 

matriz_produtos = {}
for i in range(1, len(lista)):
    matriz_produtos[lista[i][0]] = lista[i]

#fechando o aquivo do excel

dataset.close()

id_ = 0
titulo = 1
preco = 2
list_preco = 3
categor_nome = 4
best_seller = 5
comprado_ultimo_mes = 6

#criando listas especificas de cada categoria a partir do dicionario

id_lista = []
for d in matriz_produtos:
    id_lista.append(matriz_produtos[d][0])

titulo_lista = []
for a in matriz_produtos:
    titulo_lista.append(matriz_produtos[a][1])

preco_lista = []
for b in matriz_produtos:
    preco_lista.append(float(matriz_produtos[b][2]))

td_categorias=[]
for c in matriz_produtos:
    td_categorias.append(matriz_produtos[c][4])

best_lista=[]
for e in matriz_produtos:
	best_lista.append(matriz_produtos[e][5])

comprado_mes = []
for f in matriz_produtos:
    comprado_mes.append(matriz_produtos[f][6])

#A função conta quantas categorias aparecem no dicionario

def qtd_categ():
    lista = {}

    #adiciona as categorias de produtos que nao aparecem anteriormente em uma lista
    for i in td_categorias:
        quant = td_categorias.count(i)
        if i not in lista:
            lista[i] = quant

    for tipos in lista:
       print('%s = %s' % (tipos,lista[tipos]))

#A função conta quantos por cento existem de um produto nas categorias apresentadas

def percent_categ():
    list_categ = []
    #adiciona as categorias de produtos que nao aparecem anteriormente em uma lista

    for t in td_categorias:
        if t not in list_categ:
            list_categ.append(t)

    for i in list_categ:
        porcentual = (td_categorias.count(i) / len(td_categorias)) * 100

        print(f'{i} = {porcentual} %')

#A função calcula a quantidade e a proporção de produtos best sellers por categoria, calculando quantos ‘true’ tem em cada categoria e dividindo pela quantidade total de produtos

def best_tipo():
    best_ptipo = []

    for categoria in set(td_categorias):
        total_tipo = td_categorias.count(categoria)
        count = sum(1 for cat, best in zip(td_categorias, best_lista) if cat == categoria and best.lower() == 'true')
        proporcao = count / total_tipo
        best_ptipo.append([categoria, count, proporcao])

    print('Número de produtos que são best seller por tipo:')
    for categoria, count, proporcao in best_ptipo:
        print(f'Tipo: {categoria}, Best Sellers: {count}, Proporção: {proporcao:.2%}')

#A função combina quatro listas em uma lista de tuplas, ordena essa lista pelo preço, e imprime os dados dos 10 itens com menores e maiores preços.

def bar_car10(id_lista, preco_lista, titulo_lista, td_categorias):
    combinacao = list(zip(id_lista, preco_lista, titulo_lista, td_categorias))
    combinacao_ordenado = sorted(combinacao, key=lambda x: x[1])
    menores10 = combinacao_ordenado[:10]
    maiores10 = combinacao_ordenado[-10:]

    print("10 menores valores e seus respectivos dados:")
    for id_item, preco_item, titulo_item, categoria_item in menores10:
        print(f'Id:{id_item}, Preço:{preco_item}, Titulo:{titulo_item}, Categoria:{categoria_item}')

    print("10 maiores valores e seus respectivos dados:")
    for id_item, preco_item, titulo_item, categoria_item in maiores10:
        print(f'Id:{id_item}, Preço:{preco_item}, Titulo:{titulo_item}, Categoria:{categoria_item}')
        
#A função solicita ao usuário uma categoria, cria um arquivo HTML nomeado com essa categoria, e escreve uma tabela contendo ID, título, preço e se é best-seller ou não para cada produto dessa categoria.

def gerar_relatorio_por_categoria():
    cat_escolhida = input('Qual categoria será o relatório: [Moda, Esportes, Livros, Casa, EletrÃ´nicos] ')
    nom_arq = f'relatorio_produtos_{cat_escolhida}.html'
    
    with open(nom_arq, 'w') as file:
        file.write(f'<html><head><title>Relatório de Produtos - {cat_escolhida}</title></head><body>')
        file.write(f'<h1>Produtos da Categoria: {cat_escolhida}</h1>')
        file.write('<table border="1">')
        file.write('<tr><th>ID</th><th>Título</th><th>Preço</th><th>Best Seller</th></tr>')
        
        for i in range(len(td_categorias)):
            if td_categorias[i] == cat_escolhida:
                id_produto = id_lista[i]
                titulo_produto = titulo_lista[i]
                preco_produto = preco_lista[i]
                is_best_seller = 'Sim' if best_lista[i].strip().lower() == 'true' else 'Não'
                
                file.write(f'<tr><td>{id_produto}</td><td>{titulo_produto}</td><td>R${preco_produto:.2f}</td><td>{is_best_seller}</td></tr>')
        
        file.write('</table></body></html>')
        print("Relatório gerado com sucesso")
    
    return nom_arq

#A função começa filtrando os produtos que são best seller, agrupa eles por categoria, em seguida ordena os por quantidade vendida e separa os Top 10 por categoria, termina gerando o HTML

def gerar_relatorio_top10():
    best_sellers = [
        {'id': id_lista[i], 'titulo': titulo_lista[i], 'preco': preco_lista[i], 'categoria': td_categorias[i], 'best_seller': best_lista[i], 'comprado_ultimo_mes': comprado_mes[i]}
        for i in range(len(best_lista)) if best_lista[i].lower() == 'true'
    ]

    produtos_por_categoria = {}
    for produto in best_sellers:
        categoria = produto['categoria']
        if categoria not in produtos_por_categoria:
            produtos_por_categoria[categoria] = []
        produtos_por_categoria[categoria].append(produto)
    
    top_10_por_categoria = {}
    for categoria, produtos in produtos_por_categoria.items():
        produtos_ordenados = sorted(produtos, key=lambda x: x['comprado_ultimo_mes'], reverse=True)
        top_10_por_categoria[categoria] = produtos_ordenados[:10]
  
    with open('relatorio_top_10_best_sellers.html', 'w') as f:
        f.write('<html><body>\n')
        f.write('<h1>Relatório de Top 10 Best-Sellers por Categoria</h1>\n')
        for categoria, produtos in top_10_por_categoria.items():
            f.write(f'<h2>{categoria}</h2>\n')
            f.write('<table border="1">\n')
            f.write('<tr><th>Título</th><th>Quantidade Vendida</th></tr>\n')
            for produto in produtos:
                f.write(f'<tr><td>{produto["titulo"]}</td><td>{produto["comprado_ultimo_mes"]}</td></tr>\n')
            f.write('</table>\n')
        f.write('</body></html>\n')

    print("Relatório gerado com sucesso")

#loop para o menu funcional

while True :
    print("""------------------------------------------------------ 
[1] - Quantidade de produtos por Categoria
[2] - Porcentual de Produtos por Categoria
[3] - Proporção de Best-sellers por Categoria
[4] - Os 10 produtos mais baratos e mais caros
[5] - Gerar relatório HTML de produtos por categoria
[6] - Gerar relatório HTML com os Top 10 Best-sellers
[7] - Sair
------------------------------------------------------ \n """)

    opc = int(input('Opção>>>> '))

    if opc == 1:
        qtd_categ()
        print('\n')

    if opc == 2:
        percent_categ()
        print('\n')

    if opc == 3:
        best_tipo()
        print('\n')

    if opc == 4:
        bar_car10(id_lista, preco_lista, titulo_lista, td_categorias)
        print('\n')

    if opc == 5:
        gerar_relatorio_por_categoria()
        print('\n')

    if opc == 6:
        gerar_relatorio_top10()
        print('\n')

    if opc == 7:
        print('Você saiu')
        break
