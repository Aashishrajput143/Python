n=int(input('Enter the Number:'))
fact=1
if(n<0):
    print('factorial does not exist for negative number')
else:
    for i in range(1,n+1):
        fact=fact*i
    print('factorial of',n,'is',fact)
