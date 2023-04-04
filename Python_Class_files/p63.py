amt=int(input("enter amount:"))
if(amt>=1000):
    amt=amt-50
    print("50 cashback added")
    pc=input("enter promocode:")
    if(pc=="india"):
        amt=amt-50
        print("50 cashback added for pc")
    else:
        print("invalid promocode")
print("Final Amount:",amt)
