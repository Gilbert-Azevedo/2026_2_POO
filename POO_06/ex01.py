x = { "RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife" }
print(x, type(x))
print(x["RN"])
x["PB"] = "JP"
x["AM"] = "Manaus"
print(x)
#print(x["PA"])

for item in x.items(): 
    print(item, item[0], item[1], type(item))


x.pop("RN")
print(x)


x = {}
y = []
z = ()

print(type(x), type(y), type(z))


