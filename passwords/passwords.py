#Ran the below code with the line: time python3 passwords.py > [name of file here].
#I used numberOfHashes to store the number of hashes and then used another bit of code to go 
#through and delete all of the lines with the number of hashes. I didn't think it was nessecary
#to share that code.

import hashlib
import binascii

def phaseOne():

    words = [line.strip().lower() for line in open('words.txt')]

    passwords = [line.strip().lower() for line in open('hashes.txt')]

    mydict = {
        "marmot": "fbcc4e1a830c7686e09d4d89ba37367705c118f4f31d8abdb0b5c471df0792d3"
    }

    #numberOfHashes = 0

    for word in words:

        encoded_word = word.encode('utf-8') # type=bytes

        hasher = hashlib.sha256(encoded_word)
        digest = hasher.digest() # type=bytes

        digest_as_hex = binascii.hexlify(digest) # weirdly, still type=bytes

        digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string
        mydict.update({digest_as_hex_string: word})
        #numberOfHashes += 1

    for password in passwords:
        username = password.split(':')[0]
        hashed_password = password.split(':')[1]
        print(username + ":" + mydict.get(hashed_password))
        #print("Number of hashes: " + str(numberOfHashes))

def phaseTwo():
    
    #numberOfHashes = 0

    words = [line.strip().lower() for line in open('words.txt')]

    passwords = [line.strip().lower() for line in open('hashes2.txt')]

    mydict = {
        "fbcc4e1a830c7686e09d4d89ba37367705c118f4f31d8abdb0b5c471df0792d3": "jondich"
    }

    for password in passwords:
        username = password.split(':')[0]
        hashed_password = password.split(':')[1]
        mydict.update({hashed_password: username})


    for word1 in words:
        for word2 in words:

            word = word1 + word2
            
            encoded_word = word.encode('utf-8') # type=bytes

            hasher = hashlib.sha256(encoded_word)
            digest = hasher.digest() # type=bytes

            digest_as_hex = binascii.hexlify(digest) # weirdly, still type=bytes

            digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string

            #numberOfHashes += 1

            if mydict.get(digest_as_hex_string) != None:
                print(mydict.get(digest_as_hex_string) + ":" + word)
                #print("number of hashes: " + str(numberOfHashes))

def phaseThree():
    #numberOfHashes = 0

    words = [line.strip().lower() for line in open('words.txt')]

    passwords = [line.strip().lower() for line in open('hashes3.txt')]

    for password in passwords:
        username = password.split(':')[0]
        salt = password.split('$')[2]
        hashed_password = password.split('$')[3].split(':')[0]

        for word in words:

            word_and_salt =  salt + word


            encoded_word_and_salt = word_and_salt.encode('utf-8') # type=bytes

            hasher = hashlib.sha256(encoded_word_and_salt)
            digest = hasher.digest() # type=bytes

            digest_as_hex = binascii.hexlify(digest) # weirdly, still type=bytes

            digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string

            #numberOfHashes += 1

            if (digest_as_hex_string == hashed_password):
                print(username + ":" + word)
                #print("number of hashes = " + str(numberOfHashes))
                break

if __name__=="__main__": 
    phaseOne() 