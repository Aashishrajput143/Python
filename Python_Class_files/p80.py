while(True):
    a=int(input("enter 1st num:"))
    b=int(input("enter 2nd num:"))
    op=input("""Select Option:
    1.Add
    2.Mul
    """)
    if(op=="1"):
        print(a+b)
    elif(op=="2"):
        print(a*b)
    else:
        print("invalid option")

    ch=input("do you want to run it again(y/n)?")
    if(ch=="n"):
        break
    
