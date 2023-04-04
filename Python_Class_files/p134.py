#list comprehension
l=[i if(i%2==0) else i+1 for i in range(3)]
print(l)

l=[]
for i in range(3):
    if(i%2==0):
        l.append(i)
    else:
        l.append(i+1)
print(l)
