words = input('Please enter the words: ')
shift = int(input('Please enter the shift: '))

def encrypt(text):
    textlength = len(text)
    result = ''
    for i in range(textlength):
        if text[i].isupper():
            shiftcode = ord(text[i]) + shift - 65
            result += chr(shiftcode % 26 + 65)
        else:
            shiftcode = ord(text[i]) + shift - 97
            result += chr(shiftcode % 26 + 97)
    return result

def decrypt(text):
    textlength = len(text)
    result = ''
    for i in range(textlength):
        if text[i].isupper():
            shiftcode = ord(text[i]) - shift - 65
            result += chr(shiftcode % 26 + 65)
        else:
            shiftcode = ord(text[i]) - shift - 97
            result += chr(shiftcode % 26 + 97)
    return result

encryptPwd = encrypt(words)
decryptPwd = decrypt(encryptPwd)

print(encryptPwd)
print(decryptPwd)