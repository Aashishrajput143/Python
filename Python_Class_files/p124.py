x=[10,20,10,10,30,10,40,10,10]
print(x)

e=x.pop()
print(x,e)

e=x.pop(1)  #index
print(x,e)

del x[0]
print(x)

x.clear()
print(x)
