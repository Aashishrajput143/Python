y=100
def show():
    x=10
    def disp(): #closure fun
        z=30
        print("this is disp",x,y,z)
    disp()

show()
#inside disp():
    #z---->local var of disp
    #x---->nonlocal var
    #y---->global var
