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
alphabet = "abcdefghijklmnñopqrstuvwxyz1234567890"
 
# Scroll key
key = int (input("KEY: "))

if key > 0 and key <= 37:
    # Decrypted text variable
    decrypted_text = ""
    
    # Cesar Decrypt method
    for et in encrypted_text:
        if et == et.upper():
            if et.lower() in alphabet:
                decrypted_text += alphabet[((alphabet.index(et.lower()) - key) % (len(alphabet)))].upper()
            else:
                if et == " ":
                    decrypted_text += et
                else:
                    decrypted_text += ""
        else:
            if et in alphabet:
                decrypted_text += alphabet[((alphabet.index(et) - key) % (len(alphabet)))]
            else:
                if et == " ":
                    decrypted_text += et
                else:
                    decrypted_text += ""
    
    # Print Decrypted text
    print("DECRYPTED TEXT: ",decrypted_text)

    outputFile = open('message_decrypted.txt','w')
    outputFile.write(decrypted_text)
    outputFile.close()
else:
    print("Key out of range")