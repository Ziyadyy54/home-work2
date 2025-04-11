try:
    inputfromuser=int(input("enter your age"))
    if (inputfromuser%2==0):
        print("its an even number")
    else:
        print("its not a even number")
except ValueError :
    print("enter a number please")

    