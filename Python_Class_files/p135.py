#list comprehension
l=[i*j for i in range(3) for j in range(4)]
print(l)

l=[]
for i in range(3):
    for j in range(4):
        l.append(i*j)
print(l)
