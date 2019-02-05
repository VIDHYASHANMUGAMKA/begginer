n=int(input("Enter the number:"))
if(n<1 or (n%1)!=0):
    print("wrong input")
else:
    temp=0
    while(n!=0):
        temp=temp+n
        n=n-1
    print (temp) 
k=int(input("Enter the number:"))
if(k<1 or (k%1)!=0):
    print("wrong input")
else:
    temp=0
    while(k!=0):
        temp=temp+k
        k=k-1
    print (temp) 
