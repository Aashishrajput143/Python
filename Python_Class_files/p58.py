marks=float(input("enter marks:"))
if(marks>=0 and marks<30):
    print("fail")
if(marks>=30 and marks<45):
    print("3rd div")
if(marks>=45 and marks<60):
    print("2nd div")
if(marks>=60 and marks<=100):
    print("1st div")
if(marks>100 or marks<0):
    print("invalid marks")
print("bye")
