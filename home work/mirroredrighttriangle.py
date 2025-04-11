inputfromuser=int(input("enter a number to make a triangle "))
for i in range (1,inputfromuser):
    for k in range (inputfromuser-i):
        print(" ",end="")
    for n in range (i):
        print(". ",end="")  
    print("")