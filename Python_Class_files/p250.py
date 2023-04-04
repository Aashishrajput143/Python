#generator fun
def myrange(x,y):
    while(x<y):
        yield x
        x+=1

for i in myrange(1,5):
   print(i) 
print("----------")
for i in myrange(10,20):
   print(i) 
