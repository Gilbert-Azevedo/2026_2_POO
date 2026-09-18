x = []
y = list()
print(type(x))
print(type(y))

x.append(10)
x.append(20)
z = x
z.append(30)
x = [40]
print(x)
print(y)
print(z)
print(x[0])
x.append(z)
print(x)  # [40, [10, 20, 30]]
print(len(x))  # função
print(x[1][2])

# print(x.len()) se fosse um método

#print(int("Teste")) # ValueError
#print(x[5])         # IndexError
#print(1/0)          # ZeroDivisionError

x = int()
x = 0
print(x)
#raise ValueError()




