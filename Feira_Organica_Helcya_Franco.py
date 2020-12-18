frutas = {'Banana':2.00, 'Maçã': 3.50, 'Laranja':2.20, 'Melancia': 3.00, 'Maracujá': 1.40, 'Melão':1.50}

verduras = {'Rúcula': 1.40, 'Acelga': 5.33,'Couve-Flor': 7.90, 'Alface': 1.00, 'Brócolis':9.99, 'Repolho':2.20}

legumes = {'Tomate': 3.59,'Pepino': 2.60, 'Chuchu': 4.30,  'Cebola': 5.50, 'Cenoura': 3.99, 'Batata': 4.40}

diversos = {'Ovo': 10.00, 'Mel': 8.60, 'Vinagre': 3.20, 'Farofa': 5.90, 'Manteiga': 6.00, 'Leite': 4.70}

cesta = []
total = []
choice = 0
answer = str

import getpass
usuario = getpass.getuser()

def pagamento():
        print('''
            ====================================
            | ESCOLHA SUA FORMA DE PAGAMENTO : |
            ====================================
            | (1) - CARTÃO DE CRÉDITO          |
            ------------------------------------
            | (2) - CARTÃO DE DÉBITO           |
            ------------------------------------
            | (3) - DINHEIRO                   |
            ====================================        
        ''')

def menu_secao():
        print('==================')
        print('|     FRUTAS     |')
        print('==================')
        print('| ITEM\tVALOR |')
        print('==================')
        for item in frutas:
            print(item,'......',frutas[item],'\n')
        
        print('================')
        print('|   VERDURAS   |')
        print('=================')
        print('| ITEM\tVALOR |')
        print('=================')
        for item in verduras:
            print(item,'......', verduras[item],'\n')
            
        print('===============')
        print('|   LEGUMES   |')
        print('===============')
        print('| ITEM\tVALOR |')
        print('===============')
        for item in legumes:
            print(item,'......', legumes[item],'\n')
            
        print('================')
        print('|  DIVERSOS  |')
        print('================')
        print('| ITEM\tVALOR |')
        print('================')
        for item in diversos:
            print(item,'......', diversos[item]) 
               
def menu_principal():
        print('''
                ================================================
                |   Seja Bem-Vindo(a) à Feira Orgânica Online! |
                ================================================
                | (1) - ADICIONAR ITENS À CESTA DE COMPRAS     |
                ------------------------------------------------
                | (2) - SAIR                                   |
                ================================================
        ''')

while choice != 2:        
    menu_principal()        
    choice = input('Insira a opção de sua escolha:')
    if choice == '1':
        nomeDict = (frutas, verduras, legumes, diversos)
        menu_secao()
        while answer != 'Sair':
            answer = input('\nDigite o produto que você deseja comprar :\n'
                       '(Digite SAIR para terminar)').capitalize()
            for nome in nomeDict:
                if answer in nome.keys():                    
                    cesta.append(answer)
                    qnty = int(input('Digite a quantidade do produto:'))
                    cesta.append(qnty)
                    total.append(nome[answer] * qnty)
                    break
                elif str(nome) == 'diversos':
                    print('Produto não encontrado!')                                                                  
        print(f'\nEstes são os itens adicionados a sua cesta de compras: {cesta}') 
    for values in cesta:
        valor_total = sum(total)
        print(f'\nO valor total de suas compras é: R$ {valor_total}')
        forma_pag = str
        endereco = str
        nome = str
        pagamento()                
        escolha_pag = input('\nEscolha a sua forma de pagamento:')                
        if escolha_pag == '1':
            forma_pag = 'Cartão de Crédito'
        if escolha_pag == '2':
            forma_pag = 'Cartão de Débito'
        if escolha_pag == '3':
            forma_pag = 'Dinheiro'                    
        endereco = input('Digite o endereço para entrega dos produtos:')
        nome = input('Digite o nome de quem receberá os produtos:')
        print('A Nota Fiscal será exibida na Área de Trabalho.')
        arquivo = open('C:\\Users\\' + usuario + f'\\Desktop\\Nota_Fiscal_{nome}.txt', 'w')
        arquivo.write('NOTA FISCAL\n')
        arquivo.write(f'NOME: {nome}\n')
        arquivo.write(f'ENDEREÇO:{endereco}\n')
        arquivo.write(f'LISTA DE COMPRAS:')
        arquivo.write(f'ITEM / QUANTIDADE: {cesta}\n')
        arquivo.write(f'VALOR TOTAL: {valor_total} reais\n')
        arquivo.close()  
        quit()
    if choice == '2':
        quit()



        



          





 
 
 
 
 

