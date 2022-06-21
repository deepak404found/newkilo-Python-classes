import string

test_msg = "13-18-.- -1-13-1-14- -19-9-14-7-8-,- -9-19- -6-18-9-5-14-4- -15-6- -4-5-5-16-1-11"


alphabets = [alpha for alpha in 'abcdefghijklmnopqrstuvwxyz']

decoded_message = []

for a in test_msg.split("-"):
    if (a not in [" ", ".", ","]):
        decoded_message.append(alphabets[int(a) - 1])
    else:
        decoded_message.append(a)

print(''.join(decoded_message))
