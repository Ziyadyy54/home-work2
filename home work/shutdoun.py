def shutdown():
    inputfromuser=str(input("do you want to shutdown (yes/no)"))
    if inputfromuser.lower()=="yes":
        print("shuting down")
    elif inputfromuser.lower()=="no":
        print("abord shutdown")
    else:
        print("invalid answer please try again")
if __name__ == "__main__":
    print("Welcome to the Shutdown Program!")
    shutdown()
    print("Program ended.")