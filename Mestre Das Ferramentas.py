#JOSÉ LUCAS ALBUQUERQUE DE ANDRADE
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
    data['clientes'] = []
    data['clientesDados'] = []
    data['apurado'] = 0
    data['quantidadeVendida'] = 0
# Começo das funções
# Função Menu


def menu(valor):
    if valor == "CADASTRO":
        app.removeAllWidgets()
        app.setBgImage("background.gif")
        app.addLabel("inicio", "Mestre Das Ferramentas", 0, 0)
        app.entry("Produto:", label=True)
        app.setEntryUpperCase("Produto:")
        app.entry("Valor do Produto:", label=True)
        app.entry("Quantidade:", label=True)
        app.addButton("Salvar", salvar)
    if valor == "CLIENTES":
        app.removeAllWidgets()
        app.setBgImage("background.gif")
        app.addLabel("inicio", "Mestre Das Ferramentas", 0, 0)
        app.entry("Nome:", label=True)
        app.setEntryUpperCase("Nome:")
        app.addLabelEntry("CPF:")
        app.entry("Endereço:", label=True)
        app.setEntryUpperCase("Endereço:")
        app.addButton("Cadastrar", cadastro)
    if valor == "LISTA CLIENTES":
        app.removeAllWidgets()
        app.setBgImage("background.gif")
        app.addLabel("inicio", "Mestre Das Ferramentas", 0, 0)
        lista = ""
        for indice, elemento in enumerate(data['clientesDados']):
            lista = lista + "Nome: " + str(data['clientes'][indice]) + " CPF: "+ str(data['clientesDados'][indice][0]) \
                   + " Endereço: " + str(data['clientesDados'][indice][1]) + "\n"
        app.addScrolledTextArea("Lista de Produtos", text=lista)
    if valor == "AJUSTE CLIENTES":
        app.removeAllWidgets()
        app.setBgImage("background.gif")
        app.addLabel("inicio", "Mestre Das Ferramentas", 0, 0, 2)
        app.addLabelAutoEntry("Nome:", data['clientes'], 1, 0, 2)
        app.setEntryUpperCase("Nome:")
        app.addLabelEntry("Novo Nome:", 2, 0, 2)
        app.setEntryUpperCase("Novo Nome:")
        app.addLabelEntry("CPF:", 3, 0, 2)
        app.addLabelEntry("Endereço:", 4, 0, 2)
        app.setEntryUpperCase("Endereço:")
        app.addButton("Alterar", alterarCadastro, 5, 0)
        app.addButton("Remover Cliente", removerCliente, 5, 1)
    if valor == "PESQUISA":
        pesquisa = app.stringBox("Pesquisa", "Digite o nome do Item para Pesquisa:")
        if pesquisa == "" or pesquisa is None:
            pesquisa = " "
        x = 0
        retornoPesquisa = ""
        while x < len(data['produtos']):
            if pesquisa.upper() == data['produtos'][x][0:len(pesquisa)]:
                retornoPesquisa = retornoPesquisa + str(data['produtos'][x]) + " R$:" + str(data['preco'][x]) + "\n"
            x = x+1
        app.infoBox("Lista de Produtos", "Produtos achados:\n" + retornoPesquisa)
    if valor == "PRODUTO":
        app.removeAllWidgets()
        app.setBgImage("background.gif")
        app.addLabel("inicio", "Mestre Das Ferramentas", 0, 0)
        lista = ""
        x = 0
        while x < len(data['produtos']):
            lista = lista + data['produtos'][x] + "  R$:" + str(data['preco'][x]) + "   Quantidade:" + \
                    str(data['quantidade'][x]) + "\n"
            x = x + 1
        app.addScrolledTextArea("Lista de Produtos", text=lista)
        app.addButton("Criar lista", arquivoLista)
    if valor == "ALTERAR":
        app.removeAllWidgets()
        app.setBgImage("background.gif")
        app.addLabel("inicio", "Mestre Das Ferramentas")
        app.addLabelAutoEntry("Item:", data['produtos'])
        app.setEntryUpperCase("Item:")
        app.entry("Quantidade:", label=True)
        app.addButton("Alterar", atualizacao)
    if valor == "VENDA":
        app.removeAllWidgets()
        app.setBgImage("background.gif")
        app.addLabel("inicio", "Mestre Das Ferramentas", 0, 0, 2)
        app.addLabelAutoEntry("Cliente:", data['clientes'], 1, 0, 2)
        app.setEntryUpperCase("Cliente:")
        app.addLabelAutoEntry("Produto:", data['produtos'], 2, 0, 2)
        app.setEntryUpperCase("Produto:")
        app.addLabelEntry("Valor:", 3, 0, 2)
        app.addButton("Realizar Venda", venda, 4, 0)
        app.addButton("Valor do Produto", adcionar, 4, 1)
    if valor == "REMOVER":
        app.removeAllWidgets()
        app.setBgImage("background.gif")
        app.addLabel("inicio", "Mestre Das Ferramentas", 0, 0)
        app.addLabelAutoEntry("Produto:", data['produtos'])
        app.setEntryUpperCase("Produto:")
        app.addButton("Remover Produto", remover)
    if valor == "RELATÓRIO":
        app.removeAllWidgets()
        app.setBgImage("background.gif")
        app.addLabel("inicio", "Mestre Das Ferramentas", 0, 0)
        app.addLabel("Apurado", "Valor Apurado em Vendas:R$ " + str(data['apurado']))
        app.addLabel("Vendidos", "Quantidade de Itens Vendidos: " + str(data['quantidadeVendida']))
        app.addButton("Relatorio de Produtos Vendidos", arquivoVendas)


# função Menu Salvar
def salvar(valorBotao):
    if valorBotao == "Salvar":
        if app.getEntry("Produto:") != "" and app.getEntry("Valor do Produto:") != "" and app.getEntry("Quantidade:")\
                != "":
            produto = str(app.getEntry("Produto:"))
            try:
                valor = float(app.getEntry("Valor do Produto:"))
                quantidade = float(app.getEntry("Quantidade:"))
                if quantidade >= 0 and app.getEntry("Produto:") not in data['produtos']:
                    data['produtos'].append(produto)
                    data['preco'].append(valor)
                    data['quantidade'].append(quantidade)
                    app.infoBox("Salvo", "Produto Salvo com sucesso!")
                    app.clearEntry("Produto:")
                    app.clearEntry("Valor do Produto:")
                    app.clearEntry("Quantidade:")
                else:
                    app.infoBox("Quantidade", "Quantidade Invalida ou Produto já adcionado")
            except ValueError:
                app.warningBox("Valor Invalido", "Valor inserido não é inteiro.")
        else:
            app.warningBox("Sem Dados", "Campo(s) Vazios")


#Função Menu Alterar Quantidade
def atualizacao(valorBotao):
    if valorBotao == "Alterar":
        try:
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
            if data['quantidade'][indice] > 0 and app.getEntry('Cliente:') in data['clientes']:
                valor = float(app.getEntry("Valor:"))
                cliente = str(app.getEntry('Cliente:'))
                data['quantidadeVendida'] = data['quantidadeVendida'] + 1
                data['apurado'] = data['apurado'] + valor
                data['quantidade'][indice] = data['quantidade'][indice] - 1
                data['itensVendidos'].append([data['produtos'][indice], valor, cliente])
                app.infoBox("Venda", "Venda Cadastrada!")
            else:
                app.infoBox("Sem Estoque", "Produto Sem Estoque e/ou Cliente Não Cadastrado")
        except:
            app.infoBox("Produto Não Cadastrado", "Valor Invalido e/ou Produto Não Cadastrado e/ou Cliente não cadastra"
                                                  "do")


#Função Para Preencher o Valor
def adcionar(valorBotao):
    if valorBotao == "Valor do Produto":
        try:
            indice = data['produtos'].index(app.getEntry("Produto:"))
            app.setEntry("Valor:", data['preco'][indice])
        except:
            app.warningBox("Error", "Erro Para Conseguir Valor do Produto ou Produto Inexistente")


#função Para criar arquivos com vendas
def arquivoVendas(valorBotao):
    if valorBotao == "Relatorio de Produtos Vendidos":
        relatorio = open("relatorio.txt", 'w')
        relatorio.write("Valor Apurado em Vendas:R$ " + str(data['apurado']) + "\n")
        relatorio.write("Quantidade de Itens Vendidos: " + str(data['quantidadeVendida']) + "\n")
        x = 0
        while x < len(data['itensVendidos']):
            relatorio.write(str(data['itensVendidos'][x][0]) + "  R$:"+ str(data['itensVendidos'][x][1]) + " Cliente:"
                            +str(data['itensVendidos'][x][2]) + "\n")
            x = x + 1
        relatorio.close()
        app.infoBox("Relatório", "Relatório Gerado")


#função para criar arquivo de lista e quantidade de produtos
def arquivoLista(valorBotao):
    if valorBotao == "Criar lista":
        listaSalvar = ""
        x = 0
        while x < len(data['produtos']):
            listaSalvar = listaSalvar + data['produtos'][x] + "  R$:" + str(data['preco'][x]) + "   Quantidade:" + \
                    str(data['quantidade'][x]) +  "\n"
            x = x + 1
        relatorioLista = open("Lista de Produtos.txt", 'w')
        relatorioLista.write(listaSalvar)
        relatorioLista.close()
        app.infoBox("Gerado", "Lista Gerada")


#função de remover produtos:
def remover(valorBotao):
    if valorBotao == "Remover Produto":
        if str(app.getEntry("Produto:")) in data['produtos']:
            indice = data['produtos'].index(app.getEntry("Produto:"))
            del data['produtos'][indice]
            del data['preco'][indice]
            del data['quantidade'][indice]
            app.infoBox("Removido", "Produto Removido Com Sucesso")
        else:
            app.infoBox("Não Encontrado", "Produto Não Cadastrado No Sistema")


#função cadastro Cliente
def cadastro(valorBotao):
    if valorBotao=="Cadastrar":
        x = False
        for teste in data['clientes']:
            if app.getEntry("Nome:") == teste:
                x = True
        if x is False:
            data["clientes"].append(app.getEntry("Nome:"))
            data["clientesDados"].append([app.getEntry("CPF:"), app.getEntry("Endereço:")])
            app.clearEntry("Nome:")
            app.clearEntry("CPF:")
            app.clearEntry("Endereço:")
            app.infoBox("Cadastrado", "Cadastro feito Com Sucesso")
        else:
            app.infoBox("Cadastro", "Cliente Com Mesmo Nome Já Encontrado")


#função ajuste Cliente
def alterarCadastro(valorBotao):
    if valorBotao == "Alterar":
        x = False
        for indice, teste in enumerate(data['clientes']):
            if teste == app.getEntry("Nome:"):
                data['clientes'][indice] = app.getEntry("Novo Nome:")
                data['clientesDados'][indice][0] = app.getEntry("CPF:")
                data['clientesDados'][indice][1] = app.getEntry("Endereço:")
                app.clearEntry("Nome:")
                app.clearEntry("Novo Nome:")
                app.clearEntry("CPF:")
                app.clearEntry("Endereço:")
                x = True
        if x is False:
            app.infoBox("Cadastro", "Cliente Não Encontrado")
        if x is True:
            app.infoBox("Cadastro", "Cadastro Alterado Com Sucesso")


def removerCliente(valorBotao):
    try:
        indice = data['clientes'].index(app.getEntry("Nome:"))
        del data['clientes'][indice]
        del data['clientesDados'][indice]
        app.clearEntry("Nome:")
        app.infoBox("Removido", "Cliente Removido")
    except:
        app.warningBox("Cliente Não Encontrado", "Nenhum Cliente Encontrado")


# fim das funções
app = gui("Mestre Das Ferramentas", "430x290")


app.setBg("LIGHTBLUE")
app.setBgImage("background.gif")
opcoes = ["CADASTRO", "CLIENTES", "LISTA CLIENTES", "AJUSTE CLIENTES", "PESQUISA", "PRODUTO", "ALTERAR", "VENDA",
          "REMOVER", "RELATÓRIO"]
app.addToolbar(opcoes, menu, findIcon=True)
app.addStatusbar(fields=2)
app.setStatusbar("Autor:Lucas Andrade", 0)
app.setStatusbar("Mestre Das Ferramentas v2.0", 1)
app.addLabel("inicio", "Mestre Das Ferramentas")
app.addLabel("Instruções", "1-Adicionar Produtos\n2-Cadastro Clientes\n3-Alterar Clientes\n4-Lista de Clientes"
                           "\n5-Pesquisar Produtos\n6-Exibir Lista de Produtos\n7-Alterar Quantidade\n8-Realizar Venda"
                           "\n9-Remover Produto\n10-Controle de Lucro e Vendas")
app.go()
#JOSÉ LUCAS ALBUQUERQUE DE ANDRADE