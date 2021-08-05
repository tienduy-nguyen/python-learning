def pyramid1():
    num = int(input("Enter a number of start for pyramid1: "))
    for i in range(num):
        print(i*"#")

# pyramid1()

def pyramid2():
    num = int(input("Enter a number of start for pyramid2: "))
    for i in range(num):
        print((num-i)*" " + i*"#")

# pyramid2()

def pyramid3():
    num = int(input("Enter a number of start for pyramid3: "))
    for i in range(num):
        if i%2 != 0:
            space = (num-i)//2
            print(space*" " + i*"#" + space*" ")

pyramid3()

         #
        ###
       #####
      #######
     #########
    ###########
   #############


