a = input("Enter a number: ")

try:
    a = int(a)
    b = 20 / a
    print("The answer is:", b)

except ArithmeticError:
    print("Math error!!")
except:
    print("You didn't enter a number!")
