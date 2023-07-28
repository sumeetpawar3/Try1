inp1 = int(input("Enter the number:-"))

num = inp1
number = 0           
while num!=0:
##    print("in while loop")
    digit=num%10
    number=number*10 + digit
    num=num//10
##    print(num,digit,number)

if number == inp1:
    print("Given number is pallindrome")
else:
    print("Not pallindrome")
