n=input('Enter the string:')
s1=n.find('not')
s2=n.find('poor')
if(s2>s1 and s1>0 and s2>0):
    n=n.replace(n[s1:(s2+4)],'good')
else:
    n
print(n)
