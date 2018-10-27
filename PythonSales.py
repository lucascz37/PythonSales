from appJar import gui
import shelve
data = shelve.open("DataVendas", writeback=True)

try:
    print(data['produtos'][0])
except:
    data['produtos'] = []
    data['preco'] = []
    data['quantidade'] = []
    data['itensVendidos'] = []
    data['apurado'] = 0
    data['quantidadeVendida'] = 0
# Começo das funções
# Função Menu


def menu(valor):
    if valor == "SAVE":
        app.removeAllWidgets()
        app.addLabel("inicio", "Python_Sales", 0, 0)
        app.entry("Produto:", label=True)
        app.setEntryUpperCase("Produto:")
        app.entry("Valor do Produto:", label=True)
        app.entry("Quantidade:", label=True)
        app.addButton("Salvar", salvar)
    if valor == "SEARCH":
        pesquisa = app.stringBox("Pesquisa", "Digite o nome do Item para Pesquisa:")
        if pesquisa == "" or pesquisa is None:
            pesquisa = " "
        x = 0
        retornoPesquisa = ""
        while x < len(data['produtos']):
            if pesquisa[0].upper() == data['produtos'][x][0]:
                retornoPesquisa = retornoPesquisa + str(data['produtos'][x]) + " R$:" + str(data['preco'][x]) + "\n"
            x = x+1
        app.infoBox("Lista de Produtos", "Produtos achados:\n" + retornoPesquisa)
    if valor == "PREFERENCES":
        app.removeAllWidgets()
        app.addLabel("inicio", "Python_Sales", 0, 0)
        lista = ""
        x = 0
        while x < len(data['produtos']):
            lista = lista + data['produtos'][x] + "  R$:" + str(data['preco'][x]) + "   Quantidade:" + \
                    str(data['quantidade'][x]) + "\n"
            x = x + 1
        app.addLabel("Lista de Produtos", lista)
    if valor == "SETTINGS":
        app.removeAllWidgets()
        app.addLabel("inicio", "Python_Sales", 0, 0)
        app.addLabelAutoEntry("Item:", data['produtos'])
        app.setEntryUpperCase("Item:")
        app.entry("Quantidade:", label=True)
        app.addButton("Alterar", atualizacao)
    if valor == "REFRESH":
        app.removeAllWidgets()
        app.addLabel("inicio", "Python_Sales", 0, 0)
        app.addLabelAutoEntry("Produto:", data['produtos'], 1, 0)
        app.addLabelEntry("Valor:", 2, 0)
        app.addButton("Realizar Venda", venda, 3, 0)
        app.addButton("Valor do Produto", adcionar, 3, 1)
    if valor == "PRINT":
        app.removeAllWidgets()
        app.addLabel("inicio", "Python_Sales", 0, 0)
        app.addLabel("Apurado", "Valor Apurado em Vendas:R$ " + str(data['apurado']))
        app.addLabel("Vendidos", "Quantidade de Itens Vendidos: " + str(data['quantidadeVendida']))


# função Menu Salvar
def salvar(valorBotao):
    if valorBotao == "Salvar":
        if app.getEntry("Produto:") != "" and app.getEntry("Valor do Produto:") != "" and app.getEntry("Quantidade:")\
                != "":
            produto = str(app.getEntry("Produto:"))
            try:
                valor = float(app.getEntry("Valor do Produto:"))
                Quantidade = float(app.getEntry("Quantidade:"))
                if Quantidade >= 0:
                    data['produtos'].append(produto)
                    data['preco'].append(valor)
                    data['quantidade'].append(Quantidade)
                    app.infoBox("Salvo", "Produto Salvo com sucesso!")
                    app.clearEntry("Produto:")
                    app.clearEntry("Valor do Produto:")
                    app.clearEntry("Quantidade:")
                else:
                    app.infoBox("Quantidade", "Quantidade Invalida")
            except ValueError:
                app.warningBox("Valor Invalido", "Valor inserido não é inteiro.")
        else:
            app.warningBox("Sem Dados", "Campo(s) Vazios")


#Função Menu Alterar Quantidade
def atualizacao(valorBotao):
    if valorBotao == "Alterar":
        try:
            if data['produtos'].index(app.getEntry("Item:")) and float(app.getEntry("Quantidade:")):
                indice = data['produtos'].index(app.getEntry("Item:"))
                if float(app.getEntry("Quantidade:")) >= 0:
                    data['quantidade'][indice] = float(app.getEntry('Quantidade:'))
                    app.infoBox("Alteração", "Alterado")
                else:
                    app.infoBox("Quantidade", "Quantidade Invalida")
        except:
            app.warningBox("Valor Invalido", "Alguns Dos Campos Está Incorreto")


#Função de Venda
def venda(valorBotao):
    if valorBotao == "Realizar Venda":
        try:
            indice = data['produtos'].index(app.getEntry("Produto:"))
            if data['quantidade'][indice] > 0:
                valor = float(app.getEntry("Valor:"))
                data['quantidadeVendida'] = data['quantidadeVendida'] + 1
                data['apurado'] = data['apurado'] + valor
                data['quantidade'][indice] = data['quantidade'][indice] - 1
                data['itensVendidos'].append([data['produtos'][indice], valor])
                app.infoBox("Venda", "Venda Cadastrada!")
            else:
                app.infoBox("Sem Estoque", "Produto Sem Estoque")
        except:
            app.infoBox("Produto Não Cadastrado", "Valor Invalido ou Produto Não Cadastrado")


#Função Para Preencher o Valor
def adcionar(valorBotao):
    if valorBotao == "Valor do Produto":
        try:
            indice = data['produtos'].index(app.getEntry("Produto:"))
            app.setEntry("Valor:", data['preco'][indice])
        except:
            app.warningBox("Error", "Erro Para Conseguir Valor do Produto ou Produto Inexistente")

# fim das funções
app = gui("Vendas", "378x265")


app.setBg("Grey")
opcoes = ["SAVE", "SEARCH", "PREFERENCES", "SETTINGS", "REFRESH", "PRINT"]
app.addToolbar(opcoes, menu, findIcon=True)
app.addStatusbar(fields=2)
app.setStatusbar("Autor:Lucas Andrade", 0)
app.setStatusbar("Python_Sales v3.0", 1)
app.addLabel("inicio", "Python_Sales")
app.addLabel("Instruções", "1-Adicionar Produtos\n2-Pesquisar Produtos\n3-Exibir Lista de Produtos\n4-Alterar "
                           "Quantidade\n5-Realizar Venda\n6-Controle de Lucro e Vendas")

app.go()
