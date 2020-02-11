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
alphabet = "abcdefghijklmnñopqrstuvwxyz1234567890"
# Scroll key
key = int (input("KEY: "))
 
if key > 0 and key <= 37:
    # Encrypted text variable
    encrypted_text = ""
    
    # Cesar encryption method
    for pt in plain_text:
        if pt == pt.upper():
            if pt.lower() in alphabet:
                encrypted_text += alphabet[((alphabet.index(pt.lower()) + key) % (len(alphabet)))].upper()
            else:
                if pt == " ":
                    encrypted_text += pt
                else:
                    encrypted_text += ""
        else:
            if pt in alphabet:
                encrypted_text += alphabet[((alphabet.index(pt) + key) % (len(alphabet)))]
            else:
                if pt == " ":
                    encrypted_text += pt
                else:
                    encrypted_text += ""
    
    # Print encrypted text
    print("ENCRYPTED TEXT: ",encrypted_text)

    outputFile = open('message_encrypt.txt','w')
    outputFile.write(encrypted_text)
    outputFile.close() 
else:
    print("Key out of range")
