import random
import string

lis = []
lis2 = []
print('Enter "en" to Encode or "de" to decode message')
choice = input("Enter Choice: ")
if choice.lower() == "en":
    message = input("Enter Message to Encode:")
    mes = message.split()
    for words in mes:
        a = ""
        b = ""
        for i in range(6):
            x = random.choice(string.ascii_letters).lower()
            if i < 3:
                a = a + x
            else:
                b = b + x
        if len(words) > 2:
            ca = words[0]
            cab = words[1:]
            word = cab + ca
            cart = a + word + b
            lis.append(cart)
        else:
            cam = words[::-1]
            lis.append(cam)
    print("Encoding.......")
    print("Encoded Message: ", end="")
    for i in lis:
        print(i, end=" ")
else:
    message2 = input("Enter Message to Decode: ")
    mes = message2.split()
    for words in mes:
        a = ""
        b = ""
        if len(words) > 2:
            ca = words[3:]
            cal = len(ca) - 3
            man = ca[:cal]
            ran = man[-1]
            cam = man[0:-1]
            word = ran + cam
            lis2.append(word)
        else:
            cam = words[::-1]
            lis2.append(cam)
    print("Decoding......")
    print("Decoded message: ", end="")
    for i in lis2:
        print(i, end=" ")
