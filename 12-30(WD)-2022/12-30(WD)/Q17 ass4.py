t=input('Enter the string:')
l=len(t)
if(l%4==0):
    a=t[-1::-1]
    print(a)
else:
    print(t)
