number = input("enter a number:")
if int(number) >= 0 and len(number)==1:
     print ("yes")
elif len(number) >1 :
    first_digit = number[0]
    for i in number:
        if i!= first_digit:
            print("no")
            break
        else:
            print("yes")