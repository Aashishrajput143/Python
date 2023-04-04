num=4
if(num%2==0):
    print("even")
else:
    print("odd")
   

#short hand if else
print("even" if(num%2==0) else "odd")
print(("upper even" if(num>5) else "lower even") if(num%2==0) else "odd")
