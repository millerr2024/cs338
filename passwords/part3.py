import hashlib
import binascii

words = [line.strip().lower() for line in open('words.txt')]

passwords = [line.strip().lower() for line in open('hashes3.txt')]



numberOfHashes = 0

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

        numberOfHashes += 1

        if (digest_as_hex_string == hashed_password):
            print(username + ":" + word)
            print("number of hashes = " + str(numberOfHashes))
            break
