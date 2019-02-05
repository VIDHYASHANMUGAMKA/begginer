 value = int(input("Enter any number: "))
if value > 1:
    for i in range(2, value):
        if (value % i) == 0:
            print(" not")
            break
    else:
        print( "yes")
else:
    print( "yes")
