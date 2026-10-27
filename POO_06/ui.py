from cliente import Cliente
from clientedao import ClienteDAO

class UI:
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
    def menu():
        print("1 - Inserir, 2 - Listar, 9 - Fim")
        return int(input("Informe a opção: "))
    def inserir():
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        c = Cliente(id, nome)
        ClienteDAO().inserir(c)
    def listar():
        for c in ClienteDAO().listar():
            print(c)

UI.main()