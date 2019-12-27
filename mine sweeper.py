x=int(input("Enter the number of rows:"))
y=int(input("Enter the number of columns:"))
n=int(input("Enter the number of bombs:"))
list=[]
count=0
for i in range (n):             #get bombs locations
    print(i+1)
    j=int(input("Enter the number of row of bomb:"))
    k=int(input("Enter the number of column of bomb:"))
    print("")
    if j>x:                     #check locations of bombs that be in range of define row and column
        print("the number is faild!!!")
    elif k>y:
        print("the number is faild!!!")
    else:
        list.append((j,k))
for a in range(x):              #producte rows
    for b in range(y):          #product columns
        if (a+1,b+1) in list:   #print bombs
            print (" * ",end="")
        else:
            for c in range (a-1,a+2):
                for d in range (b-1,b+2):
                    if (c+1,d+1) in list:   #find number of bombs around the location
                        count+=1
            print("",count,"",end="")
            count=0
    print("\n")
