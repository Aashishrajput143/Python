t=input('Enter the sentence:')
l=t.split()
s=set(l)
for i in s:
    a=t.count(i)
    print(i,a)
