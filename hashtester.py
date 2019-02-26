import crypt
print ("This is an encryption script!!!!")

# Take this string 
encrypt = input("Input string > ")
#Standard strong Enc
encS = crypt.crypt(encrypt)
# Other encryptions
enc1 = crypt.crypt(encrypt, "MD5")
enc2 = crypt.crypt(encrypt, "BLOWFISH")
enc3 = crypt.crypt(encrypt, "SHA216")
enc4 = crypt.crypt(encrypt, "SHA512")
enc5 = crypt.crypt(encrypt, "CRYPT")
enc6 = crypt.crypt(encrypt, "HX")
#Print result
print ("\n[*] Your hashes were generated below...\n")
print ("Stndrd. Strong * " + encS)
print ("MD5\t * " + enc1)
print ("BlowFish * " + enc2)
print ("SHA216\t * " + enc3)
print ("SHA512\t * " + enc4)
print ("Crypt\t * " + enc5)
print ("Hex\t * " +  enc6)


