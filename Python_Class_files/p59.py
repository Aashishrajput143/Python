marks=float(input("enter marks:"))
if(marks>=0 and marks<30):
    print("fail")
elif(marks>=30 and marks<45):
    print("3rd div")
elif(marks>=45 and marks<60):
    print("2nd div")
elif(marks>=60 and marks<=100):
    print("1st div")
elif(marks>100 or marks<0):
    print("invalid marks")
print("bye")
