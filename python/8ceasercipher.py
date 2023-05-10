alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift):
    cipher_text = ""
    for letter in plain_text:
        position = alphabets.index(letter)
        new_position = (position + shift)%26
        new_letter = alphabets[new_position]
        cipher_text += new_letter
        
    return cipher_text


def decrypt(plain_text, shift):
    cipher_text = ""
    for letter in plain_text:
        position = alphabets.index(letter)
        new_position = ((position - shift) + 26)% 26
        new_letter = alphabets[new_position]
        cipher_text += new_letter

    return cipher_text


do = True
while(do):
    direction = input("Type 'encode' or 'decode' :")
    text = input("Enter your message : ").lower()
    shift = int(input("Enter the shift number make sure the number is less than 25 : "))

    if(direction == "encode"):
        print(encrypt(text, shift))
    if(direction == "decode"):
        print(decrypt(text, shift))

    prompt = input("would like to run the program again ? type 'yes' if wanter to else type 'no' ")
    if(prompt == "no"):
        do = False
