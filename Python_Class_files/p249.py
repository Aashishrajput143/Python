#generator fun
def myrange():
    yield 10
    yield 2.5
    yield "hi"

for i in myrange():
   print(i) 
