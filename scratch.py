from io import open

# Read file
txtFile = open('message.txt','r', encoding="utf8")
fileContent = txtFile.readlines()
txtFile.close()

# Replace returns by spaces
plain_text = ""
for fc in fileContent:
    plain_text += fc.replace("\n", " ")

# Print the plaint text
print("PLAIN TEXT: ",plain_text)

# Alphabet
alphabet = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
 
#Scroll key
key = int (input("Valor de desplazamiento: "))
 
#Encrypted text variable
encrypted_text = ""
 
#Cesar encryption method
for pt in plain_text:
    if pt in alphabet:
        encrypted_text += alphabet[(alphabet.index(pt) + key % (len(alphabet)))]
    else:
        if pt == " ":
            encrypted_text += pt
        else:
            encrypted_text += ""
 
#Print encrypted text
print("ENCRYPTED TEXT: ",encrypted_text)
