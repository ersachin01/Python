a = int(input("Enter a number: "))

if(a>=18):
    print("You are an adult.")
    print("You can vote.")


elif(a<0):
    print("You cannot enter a negative number.")

elif(a==0):
    print("You entered zero. Which is not a Valid age.")


else:
    print("You are below the age of 18. You are not an adult.")
    print("You cannot vote.")