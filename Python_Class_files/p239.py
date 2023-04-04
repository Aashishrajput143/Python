def show():
    x=10
    def disp(): #closure fun
        print("this is disp",x)
    disp()

show()
