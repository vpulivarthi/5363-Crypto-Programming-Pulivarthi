############################################
# Name: Pulivarthi Vijay Kumar
# Class: CMPS 5363 Cryptography
# Date: 27 july 2015
# Program 2- Randomized vigenere
############################################

import random

# Function for generating a keyword from a user inputted seed value.
def keywordFromSeed(seed):
   
    Letters = []

    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
    return ''.join(Letters)



##############################################################################

#Encryption function
#Passing plain text message and a key
def encrypt(plain_text_message,key):
    bV = buildVigenere(symbols,key)
    keyword = keywordFromSeed(key)
    
    #bV - calling buildVigenere
    #keyword - your keyword
    #ptmi - plain text message index
    #ki - keyword index
    #newI - New location of row found by iteration on vigenere matrix.
    #newJ - New location of coloumn found by iteration on vigenere matrix.
    def encryption(bV,keyword,ptmi,ki,plain_text_message):
        newJ, newI = 0, 0
        for i in range(1):
            for j in range(len(symbols)):
                if plain_text_message[ptmi] == bV[i][j]:
                    newJ = j
        
        
        for i in range(len(symbols)):
            for j in range(1):
                if keyword[ki] == bV[i][j]:
                    newI = i
    
        return bV[newI][newJ]
    i = 0
    cipherText = ''
    
    #Generating cipher text
    while i in range(len(plain_text_message)):
        ptmi = i
        ki = i % len(keyword)
        print(plain_text_message[ptmi])
                        
        cipherText = cipherText + encryption(bV,keyword,ptmi,ki,plain_text_message)
        i += 1        
    print(cipherText)
    return cipherText


##############################################################################

#Decryption function
#Passing cipher text message and a key
def decrypt(cipher_text_message,key):
    bV = buildVigenere(symbols,key)
    keyword = keywordFromSeed(key)
    
    #bV - calling buildVigenere
    #keyword - your keyword
    #ctmi - cipher text message index
    #ki - keyword index
    #newI - New location of row found by iteration on vigenere matrix.
    #newJ - New location of coloumn found by iteration on vigenere matrix.
    def decryption(bV,keyword,ctmi,ki,cipher_text_message):
        oldI, oldJ = 0,0
        for i in range(len(symbols)):
            for j in range(1):
                if keyword[ki] == bV[i][j]:
                    oldI = i
        
        for i in range(len(symbols)):
            if cipher_text_message[ctmi] == bV[oldI][i]:
                oldJ = i
        
        
    
        return bV[0][oldJ]

    i=0
    plainText = ''

    #Generating plain text(decoded)
    while i in range(len(cipher_text_message)):
        ctmi = i
        ki = i % len(keyword)
        print(cipher_text_message[ctmi])
        
        plainText = plainText + decryption(bV,keyword,ctmi,ki,cipher_text_message)
        i+= 1
    print(plainText)
    return plainText
##############################################################################

#Building a randomized vigenere table(matrix)
def buildVigenere(symbols,seed):
    random.seed(seed)

    n = len(symbols)

    vigenere = [[0 for i in range(n)] for i in range(n)]
    symbols = list(symbols)
    random.shuffle(symbols)
    symbols = ''.join(symbols)
    
    
    for sym in symbols:
        random.seed(seed)
        myList = []
    
        for i in range(n):
            r = random.randrange(n)
            
            if r not in myList:
                myList.append(r)
            else:
                while(r in myList):
                    r = random.randrange(n)
            
                myList.append(r)
                               
            while(vigenere[i][r] != 0):
                r = (r + 1) % n
            
            vigenere[i][r] = sym
            
    return vigenere

#Loading all the 95 characters of ascii into symbols variable.    
symbols = ''.join(chr(x) for x in range(32,127))


#Printing the matrix
def printMatrix(vigenere):
    i=0
    j=0
    k=0
    line = ""

    #To print coloumn wise 
    '''for i in range(26*26):
        line = line + vigenere[j][k]
        j = j + 1
        if j >= 26:
            print(line)
            x = set(line)
            line = ""
            j = 0
            k = k + 1'''
    
    #To print row wise       
    for i in range(95*95):
        line = line + vigenere[j][k]
        k = k + 1
        if k >= 95:
            print(line)
            x = set(line)
            line = ""
            k = 0
            j = j + 1
            

##############################################################################

