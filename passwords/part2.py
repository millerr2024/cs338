import hashlib
import binascii

words = [line.strip().lower() for line in open('words.txt')]

passwords = [line.strip().lower() for line in open('hashes2.txt')]

numberOfHashes = 0

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

        numberOfHashes += 1

        if mydict.get(digest_as_hex_string) != None:
            print(mydict.get(digest_as_hex_string) + ":" + word)
            print("number of hashes:" + str(numberOfHashes))