number = int(input("Enter the number:-"))
number1 = str(number)
len1= len(number1)


sum1=0
num = number
while num!=0:
    digit = num%10
    sum1= sum1+(digit**len1)
    num=num//10

if number == sum1:
    print("Narcissist number")
else:
    print("Not a Narcissist number")

    

             
