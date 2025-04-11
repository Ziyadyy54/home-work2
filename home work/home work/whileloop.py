inputfromuser=int(input("enter your number "))
count=0
while(inputfromuser>0):
    inputfromuser=inputfromuser//10
    count=count+1
print(count)