number = int(input("Enter a number: "))
prime = True

for i in range(2,int(number/2)):
    if number % i == 0:
        prime = False
        break

if prime == True:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
    




