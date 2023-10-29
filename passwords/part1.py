import hashlib
import binascii

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
