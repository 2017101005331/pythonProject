import random
n= random.randint(1,100)
guess=int(input("Enter the number= "))
while n!=guess:
   if (guess<n):
      print("too slow ")
      guess=int(input("enter the number again"))
   elif (guess>n):
      print("Too high")
      guess=int(input("enter the number again"))
   # if guess gets equals to n terminate the while loop
   else:
      break
print("You guess it right ")