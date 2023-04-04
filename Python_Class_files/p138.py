s=input("enter 10 nums seperated by space:")
l=s.split()
print(l)
l2=[]
for i in l:
    l2.append(int(i))
print(l2)
print(sum(l2))
