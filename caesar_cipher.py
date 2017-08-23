# =======================Note=======================
# print(ord('A')) A-Z  char to num
# print(chr(65)) 65-90 num to char
# print(chr(32)) 32 is space
# I love Valentine
# ==================================================
import sys

# caesar function
def caesar_Cipher(c,rot):
    c += rot
    if c > 90:
        c = c - 90 + 64
    return chr(c)

# encrypt function
def encrypt():
    # input and uppercase
    cipherText = input("Enter Text:\n").upper()
    # ===========output===============
    print("==========Output Text==========")
    for rot in range(1,26):
        plainText = ""
        for i in cipherText:
            if 65 <= ord(i) and ord(i) <= 90:
                plainText = plainText + caesar_Cipher(ord(i),rot)
            else:
                plainText += i
        print("rot" + str(rot) + " : " + plainText)
    print("==========DONE==========\n")

# decrypt function
def decrypt():
    # input and uppercase
    cipherText = input("Enter Text:\n").upper()
    # ===========output===============
    print("==========Output Text==========")
    for rot in range(25,0,-1):
        plainText = ""
        for i in cipherText:
            if 65 <= ord(i) and ord(i) <= 90:
                plainText = plainText + caesar_Cipher(ord(i),rot)
            else:
                plainText += i
        print("rot" + str(26-rot) + " : " + plainText)
    print("==========DONE==========\n")

# main
while True:
    print("[1]:Encrypt\n[2]:Decrypt\n[0]:Exit")
    check = int(input("Please Enter Number: "))
    if check == 1:
        encrypt()
    elif check == 2:
        decrypt()
    elif check == 0:
        input('\n----------------Press ENTER to exit----------------\n')
        sys.exit()
    else:
        print("\n*******Error*******\n")