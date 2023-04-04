amt=int(input("enter amount:"))
if(amt>=1000):
    amt=amt-50
    print("50 cashback added")
    pc=input("enter promocode:")
    if(pc=="india"):
        pct=amt*5/100
        if(pct>100):
            amt=amt-100
            print("100 cashback added for pc")
        else:
            amt=amt-pct
            print("5% cashback added for pc")
    else:
        print("invalid promocode")
print("Final Amount:",amt)
