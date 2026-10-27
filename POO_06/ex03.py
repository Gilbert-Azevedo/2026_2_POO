import json

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

a = Cliente(1, "Douglas Crockford")  #json
b = Cliente(2, "Jon Bosak")          #xml

print(a)
print(b)
print(a.__dict__)
print(vars(b))

lista = [a, b]
print(lista)
for c in lista: print(vars(c))

arquivo = open("clientes.json", mode="w")
json.dump(lista, arquivo, default = vars)
arquivo.close()
