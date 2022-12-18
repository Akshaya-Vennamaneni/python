num=int(input("Enter a number: "))
temp=num
rev=0
while(num>0):
    remainder=num%10
    rev=rev*10+remainder
    num=num//10
if(temp==rev):
    print("Palindrome")
else:
    print("Not a Palindrome")
    
