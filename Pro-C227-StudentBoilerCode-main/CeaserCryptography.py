
print("Welcme to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("encription..")
    message = input("Enter your message ")
    key = int(input("Enter Key from 1 to 94 "))
    encryptText = ""
    for i in range(len(message)):
        temp = (ord(message[i])+key)
        if temp>126:
            temp = temp-127+32
        encryptText = chr(temp)
    print("Encrpted : "+encryptText)
    main()

def decryption():
    print("Decription...")
    print("Message can only lower or upper case alphabets ")
    encryptMessage = input("Enter encrpyted text ")
    decryptKey = int(input("Enter key from 1 to 94 "))
    decryptText = ""
    for i in range(len(encryptMessage)):
        temp = (ord(encryptMessage[i])-decryptKey)
        if temp>32:
            temp = temp+127-32
        decryptText = chr(temp)
    print("Decrypted: "+decryptText)





    
    

        
if __name__ == "__main__":
    main()
