# Import libraries

import sys
import crypt

# List of Encryptions
encrypts = [
        'CRYPT',
        'SHA256',
        'SHA512',
        'BlowFish',
        'MD5',
        'HEX'
]

# Constants
HEX_ = 'yes'
ANSWER = 'yes'
CRYPT_ = 'yes'
SHA256_ = 'yes'
SHA512_ = 'yes'
BLOWFISH_ = 'yes'
MD5_ = 'yes'

# Prompt for users name
name = input("Good Day, Your name is...? > ")
# Print users name and explain what the program does
print ("\nHello {}, This program encrypts in 5 different algorithms!!!\n".format(name))

for encrypt in encrypts:
        print ("\t* " + encrypt)

# Begin asking for algorithm choices
# If yes to a algorithm choice ask for quote or string to encrypt
hash = input('\nWould you like to implement the Standard Strong Hash Encryption?(Yes/no) ')

if hash.lower() == ANSWER:
        hash = input('Ok then we will use Standard Strong encryption, enter your string/quote > ')
        print (crypt.crypt(hash))
        sys.exit(0)

CRYPT_ = input("OK then, want to use Crypt Encryption?(Yes/no) ")

if CRYPT_.lower() == 'yes':
        CRYPT_ = input("Input here for Crypt >  ")
        print (crypt.crypt(CRYPT_, "CRYPT"))
        sys.exit(0)

SHA256_ = input("OK then, want to use SHA256 Encryption?(Yes/no) ")

if SHA256_.lower() == 'yes':
        SHA256_ = input("Input your string/quote for a SHA256 Encrption > ")
        print (crypt.crypt(SHA256_, "SHA256"))
        sys.exit(0)

SHA512_ = input("Ok then want to use SHA512 Encryption?(Yes/no) ")

if SHA512_.lower() == 'yes':
        SHA512_ = input("Input your quote/string for SHA512 Encryption > ")
        print (crypt.crypt(SHA512_, "SHA512"))
        sys.exit(0)

BLOWFISH_ = input("OK then, Want to use BlowFish Encryption?(Yes/no) ")

if BLOWFISH_.lower() == 'yes':
        BLOWFISH_ = input("Input your quote/string for Blowfish Encryption > ")
        print (crypt.crypt(BLOWFISH_, "BLOWFISH"))
        sys.exit(0)

MD5_ = input("Ok then shall we use MD5 Encryption?(Yes/no) ")

if MD5_.lower() == 'yes':
        MD5_ = input("Input your string/quote here for MD5 Encryption >  ")
        print (crypt.crypt(MD5_, "MD5"))
        sys.exit(0)

HEX_ = input("Ok then shall we use HEX Encryption?(Yes/no) ")

if HEX_.lower() == 'yes':
	HEX_ = input("Input your string/quote here for HEX Encryption >  ")
	print (crypt.crypt(HEX_, "HX"))
else:
	print ("Goodbye!!!")
sys.exit(0)




