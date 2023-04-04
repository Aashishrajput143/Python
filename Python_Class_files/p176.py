#dict comprehension
#var={keyexp:valexp for}

d={i:i+i for i in "abc"}
print(d)

d={i:i*i for i in range(4)}
print(d)

d={input("enter key:"):input("enter value:") for i in range(3)}
print(d)
