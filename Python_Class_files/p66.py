a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
op=input("""Select Option:
1.Add
2.Mul
3.Div
""")

match(op):
    case "1":
        print(a+b)
    case "2":
        print(a*b)
    case "3":
        print(a/b)
    case _:
        print("invalid option")
