n=int(input('how many words u want to enter:'))
l=[input('Enter the word '+str(i+1)) for i in range(n)]
s=[len(m) for m in l]
print('length of longest one:',max(s))
