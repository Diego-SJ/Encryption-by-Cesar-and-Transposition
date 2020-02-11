from io import open

def encrypt_transposition(encrypted_text):
    # msg = input("Enter Plain Text: ").replace(" ", "").upper()
    msg = encrypted_text.replace(" ", ",")
    # print(msg)
    key = input("\n---------- Transposition keyword: ").upper()

    # assigning numbers to keywords
    kywrd_num_list = keyword_num_assign(key)

    print("\n\n========== Transposition grid ==========\n\n")
    # printing key
    for i in range(len(key)):
        print(key[i], end=" ", flush=True)
    # for
    print()
    for i in range(len(key)):
        print(str(kywrd_num_list[i]), end=" ", flush=True)
    # for
    print("\n-------------------------")

    # in case characters don't fit the entire grid perfectly.
    extra_letters = len(msg) % len(key)
    # print(extraLetters)
    dummy_characters = len(key) - extra_letters
    # print(dummyCharacters)

    if extra_letters != 0:
        for i in range(dummy_characters):
            msg += "."
    # if

    # print(msg)

    num_of_rows = int(len(msg) / len(key))

    # Converting message into a grid
    arr = [[0] * len(key) for i in range(num_of_rows)]
    z = 0
    for i in range(num_of_rows):
        for j in range(len(key)):
            arr[i][j] = msg[z]
            z += 1
        # for
    # for

    for i in range(num_of_rows):
        for j in range(len(key)):
            print(arr[i][j], end=" ", flush=True)
        print()
    # for

    # getting locations of numbers
    num_loc = get_number_location(key, kywrd_num_list)
    
    # cipher
    cipher_text = ""
    k = 0
    for i in range(len(key)):
        if k == len(key):
            break
        else:
            d = int(num_loc[k])
        # if
        for j in range(num_of_rows):
            cipher_text += arr[j][d]
        # for
        k += 1
    # for

    print("\n\n========== Final Text Encrypted ==========\n\n")
    print(cipher_text)
    
    return cipher_text

def get_number_location(key, kywrd_num_list):
    num_loc = ""
    for i in range(len(key)):
        for j in range(len(key)):
            if kywrd_num_list[j] == i:
                num_loc += str(j)
            # if
        # for
    # for
    return num_loc


def keyword_num_assign(key):
    alpha = "ABCDEFG"
    kywrd_num_list = list(range(len(key)))
    # print(kywrdNumList)
    init = 0
    for i in range(len(alpha)):
        for j in range(len(key)):
            if alpha[i] == key[j]:
                init += 1
                kywrd_num_list[j] = init - 1
            # if
        # inner for
    # for
    return kywrd_num_list

def encrypt_cesar(plain_text):
    # Alphabet
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
    # Scroll key
    key = int (input("\n---------- Cesar's key: "))
    
    if key > 0 and key <= 37:
        # Encrypted text variable
        encrypted_text = ""
        
        # Cesar encryption method
        for pt in plain_text:
            if pt in alphabet:
                    encrypted_text += alphabet[((alphabet.index(pt) + key) % (len(alphabet)))]
            else:
                if pt == " ":
                    encrypted_text += pt
                else:
                    encrypted_text += ""
        
        # Print encrypted text
        print("\n\n========== Text encrypted by cesar ==========\n\n",encrypted_text)

        return encrypted_text
    
    else:
        print("Key out of range")

def main():
    
    # Read file
    txtFile = open('message.txt','r', encoding="utf8")
    fileContent = txtFile.readlines()
    txtFile.close()

    # Replace returns by spaces
    plain_text = ""
    for fc in fileContent:
        plain_text += fc.replace("\n", " ").upper()

    # Print the plaint text
    print("\n\n========== Plain Text from message.txt file ==========\n\n",plain_text)

    # Run cesar encryption
    encrypted_text = encrypt_cesar(plain_text)

    # Run transposition encryption
    final_encryption = encrypt_transposition(encrypted_text)

    # Create output file
    outputFile = open('message_encrypt.txt','w')
    outputFile.write(final_encryption)
    outputFile.close() 
    print("\n\n========== Check message_encrypt.txt file ==========\n\n") 

if __name__ == "__main__":
    main()