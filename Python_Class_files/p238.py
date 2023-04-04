#Nested fun:if a fun is defined inside block of other fun,called nested fun
def show():                    #top level/outer fun
    print("this is show1")
    def disp():                #outer fun for display/nested fun for show
        print("this is disp1")
        def display():         #nested fun
            print("this is display")
        print("this is disp2")
        display()
    print("this is show2")
    disp()
show()
