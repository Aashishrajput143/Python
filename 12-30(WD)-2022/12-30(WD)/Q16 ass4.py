t=input('Enter the string:')
s=input('Enter the substring:')
if(s in t):
    i=s.index(s)
    print('The last character before the sub-string is',{s[i-1]})
else:
    print('substring does not exist')
