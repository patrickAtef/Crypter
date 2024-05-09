import os
from cryptography.fernet import Fernet

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def FindAllFiles(path):
    for file in os.listdir(path):
        print(file)

def Encrypt(path, key):
    with open("thekey.key", "wb") as thekey:
        thekey.write(key)

    i = 0
    for file in os.listdir(path):
        os.chdir(path)
        with open(file, "rb") as thefile:
            content = thefile.read()

        content_encrypted = Fernet(key).encrypt(content)

        with open(file, "wb") as thefile:
            thefile.write(content_encrypted)
        if i > 3 :
            break
        i = i + 1
        print(i)

def Decrypt(path):
    with open("thekey.key", "rb") as thekey:
        key = thekey.read()
    print(key)
    os.chdir(path)
    for file in os.listdir(path):
        with open(file, "rb") as thefile:
            content = thefile.read()

        content_encrypted = Fernet(key).decrypt(content)

        with open(file, "wb") as thefile:
            thefile.write(content_encrypted)
        if i > 3 :
            break
        i = i + 1

if __name__ == '__main__':
    #FindAllFiles('F:\ToEncrypt')
    key = Fernet.generate_key()
    #Encrypt('F:\ToEncrypt', key)   //el key saved fadii !!CAUTION!!
    Decrypt('F:\ToEncrypt')
