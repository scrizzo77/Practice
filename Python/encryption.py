message = input("Enter a short message: ")


def encryption(message):
    encrypted = ""
    for i in range(1, len(message), 2):
        encrypted += message[i]
        
    for i in range(0, len(message), 2):
        encrypted += message[i]

    return encrypted

encrypted = encryption(message)
print(encrypted)
