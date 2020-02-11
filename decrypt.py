from io import open

# Read file
txtFile = open('message_encrypt.txt','r', encoding="utf8")
fileContent = txtFile.readlines()
txtFile.close()

# Replace returns by spaces
encrypted_text = ""
for fc in fileContent:
    encrypted_text += fc.replace("\n", " ")

# Print the plaint text
print("ENCRYPTED TEXT: ",encrypted_text)

# Alphabet
alphabet = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
 
# Scroll key
key = int (input("KEY: "))
 
# Decrypted text variable
decrypted_text = ""
 
# Cesar Decrypt method
for pt in encrypted_text:
    if pt in alphabet:
        decrypted_text += alphabet[(alphabet.index(pt) - key % (len(alphabet)))]
    else:
        if pt == " ":
            decrypted_text += pt
        else:
            decrypted_text += ""
 
# Print Decrypted text
print("DECRYPTED TEXT: ",decrypted_text)

outputFile = open('message_decrypted.txt','w')
outputFile.write(decrypted_text)
outputFile.close()
