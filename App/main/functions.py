# • Ao executar o sistema deve mostrar um menu para o usuário digitar quais operação deseja
# realizar.
# • Cadastrar ITEM
# • Alterar ITEM
# • Excluir ITEM fornecendo o Código
# • Localizar um ITEM pelo Código
# • Listagem geral dos ITEMS (apresentando a quantidade geral, e o somatório / media dos
# valores numéricos). 
# • Item escolhido -> LIVROS (Código, Nome, Editora, Ano, ValorPago).

import json

class Book:
    def __init__(self, code, name, publisher, year, price):
        self.code = code
        self.name = name
        self.publisher = publisher
        self.year = year
        self.price = price

def option_check(option):
    if option not in [1,2,3,4,5]:
        print('[ERRO] - OPÇÃO INVÁLIDA!')
        return menu()
    elif option == 1:
        return register_book()

def register_book():
    print('\nCADASTRO DE LIVRO\n')
    code = input('CÓDIGO DO LIVRO: ').upper()
    name = input('NOME DO LIVRO: ').upper()
    publisher = input('NOME DA EDITORA: ').upper()
    year = int(input('ANO DE PUBLICAÇÃO: '))
    price = float(input('PREÇO DO LIVRO: '))
    
    book = Book(code,name,publisher,year,price)
    book_list = {
                'Código': book.code, 
                'Nome': book.name, 
                'Editora': book.publisher, 
                'Ano': book.year, 
                'Preço': book.price
                }
    print(book_list)
    
    # This is used to mannage a .json file content
    # with open('data.json') as f:
    #     data = json.load(f)
    # for state in data['states']:
    #     print(state['name'])

    # This was use to write data on a .txt file
    # with open("./data.txt",'a') as f:
    #     f.write(str(book_list))    
    #     f.write('\n')

    print('\n|CADASTRO EFETUADO COM SUCESSO!|\n')

# def change_record():

# def remove_book():

# def find_book():

# def list_books(): 

def menu():
    print('\n[1] - CADASTRAR LIVRO \n[2] - ALTERAR CADSTRO DE LIVRO \n[3] - EXCLUIR CADASTRO DE LIVRO PELO CÓDIGO \n[4] - LOCALIZAR LIVRO PELO CÓDIGO \n[5] - LISTAR ITENS')
    option = int(input('Digite qual operação você deseja fazer: '))
    option_check(option)