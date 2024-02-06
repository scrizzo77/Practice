# We need to initialise the flags to False, because False means 0
upperFlag = False
lowerFlag = False
numberFlag = False
specFlag = False

userPwd = input("Please enter a password ")
userPwdlen = len(userPwd)

# Ask the user to enter the password until the number of characters in it is between 6 and 12
while (userPwdlen < 6 or userPwdlen > 12):
    userPwd = input("Password is not between 6 and 12 characters. Try again ")
    userPwdlen = len(userPwd)

for i in range(userPwdlen):

    if userPwd[i].isupper(): # if any character in the password is upper case, set it to True or 1
        upperFlag = True

    if userPwd[i].islower(): # if any character in the password is lower case, set it to True or 1
        lowerFlag = True

    if userPwd[i].isnumeric(): # if any character in the password is a number, set it to True or 1
        numberFlag = True

    if not userPwd[i].isalnum(): # if any character in the password is special (not alphanumeric), set it to True or 1
        specFlag = True

pwdRating = upperFlag + lowerFlag + numberFlag + specFlag
print("\npwdRating",pwdRating)

# There are four flags so the maximum total of them will be 4 (as True = 1)
if pwdRating == 4:
    print("Password is very strong")
elif pwdRating == 3:
    print("Password is strong")
elif pwdRating == 2:
    print("Password is medium")
elif pwdRating == 1:
    print("Password is weak")
else:
    print("Password is very weak")
