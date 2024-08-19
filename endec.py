import os
import random as r
############################################################################################
def check():      #CHECKS IF FOLDER IS ALREADY PERSENT
    if not os.path.isdir("E:\\Encryption-Key"):
        os.mkdir("E:\\Encryption-Key")
############################################################################################
def keypass(k):   #ENCRYPTS THE KEY IN A FILE UNDER THE DIRECTORY
    check()
    f=open("E:\\Encryption-Key\\key.txt", "w")
    z=''
    for i in str(k):
        ran=r.randint(0,9)
        z=z+i+str(ran)
    f.write(z)
    f.close()    
############################################################################################
def encrypt():    #ENCRYPTS THE TEXT
    f=open("D:\\pythonpro\\encryptiondecryption\\encryptedfile.txt", "w")
    s=input("Enter The Text You Want To Encrypt : ")
    final=''
    go=1
    while go==1:
        key=int(input('Enter a key ( DIGITS ONLY ) : '))
        if len(str(key))==7:
            go=2
            keypass(key)
            print("Key Accepted")
            print("Warning : This Key Will Be Asked At Time Of Decryption")
        elif len(str(key))<7:
            go=1
            print("Error : Key Is Having Less Than 7 Digits")
        else:
            print("Error : Key Is Having More Than 7 Digits")
    zigzag = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    wd=s.split()
    for i in wd:
        final=final+''.join(r.choices(zigzag, k=3))+i[1:]+i[0]+''.join(r.choices(zigzag, k=3))+' '
    print("File Successfully Encrypted\n")
    f.write(final)
    f.close()
############################################################################################
def decrypt()::    #DECRYPTS THE TEXT
    f=open("D:\\pythonpro\\encryptiondecryption\\encryptedfile.txt", "r")
    r=f.read()
    f.close()
    key2=int(input("Enter Your Decryption Key : "))
    fp=open("E:\\Encryption-Key\\key.txt", "r")
    g=fp.read()
    fp.close()
    nw=""
    if g=='':
        print("Encrypted Code Not Found!\n")
    else:
        nw=g[0::2]
        if key2==int(nw):
            final=''
            word=[]
            wd=r.split()
            for i in wd:
                final=i[3:-3]
                final=final[-1]+final[:-1]
                word.append(final)
            print(' '.join(word))
        else:
            print("Error : User Has Denied Access!\n")
############################################################################################
while True:
    x=int(input("Welcome To Encrypt/Decrypt Centre :-\n1 ---> Encrypt\n2 ---> Decrypt\n0 ---> Exit\n"))        
    if x==1:
        encrypt()
    elif x==2:
        decrypt()
    else:
        break
