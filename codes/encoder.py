alphabets = [alpha for alpha in 'abcdefghijklmnopqrstuvwxyz']


message = input("Enter a message: ")

secret = []

for i in message:
    if (i.lower() not in alphabets):
        dummy = i
    else:
        dummy = alphabets.index(i.lower()) + 1

    secret.append(str(dummy))

secret_message = "-".join(secret)

print("Encrypted Message: " + secret_message)
