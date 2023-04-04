s=input('Enter the string:')
d={}
for i in range(0,128):
    a=chr(i)
    b=s.count(a)
    if(b!=0):
        d[a]=b
print(d)
