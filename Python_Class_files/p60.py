marks=float(input("enter marks:"))
if(marks>=0 and marks<30):
    print("fail")
elif(marks>=30 and marks<45):
    print("3rd div")
elif(marks>=45 and marks<60):
    print("2nd div")
    print("apple")
elif(marks>=60 and marks<=100):
    print("1st div")
    print("mango")
else:
    print("invalid marks")
print("bye")
