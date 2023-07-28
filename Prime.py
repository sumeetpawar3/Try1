number = int(input("Enter the number:-"))
count=0
for i in range(2,number+1,1):
    if number%i==0:
        count=count+1

if count==1:
    print("Prime number")
   
    
