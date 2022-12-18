lowerrange=int(input("Enter the lower range: "))
upperrange=int(input("Enter the upper range: "))
print("The prime numbers in the given range are: ")
for num in range(lowerrange,upperrange+1):
    if(num>1):
        for i in range(2,num):
               if(num%i==0):
                  break
        else:
            print(num)
