#parallel iteration of multiple collections
l=[10,20,30]
t=('a','b','c')
s={100,200,300}

for i in zip(l,t,s):
   print(i) 

print("---------")
for i,j,k in zip(l,t,s):
   print(i,j,k) 
