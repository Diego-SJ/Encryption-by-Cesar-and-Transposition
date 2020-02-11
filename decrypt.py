from io import open

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


def transposition_decryption(encrypted_text):
    msg = encrypted_text
    # print(msg)
    key = input("\n---------- Transposition keyword: ").upper()

    # assigning numbers to keywords
    kywrd_num_list = keyword_num_assign(key)

    num_of_rows = int(len(msg) / len(key))

    # getting locations of numbers
    num_loc = get_number_location(key, kywrd_num_list)

    # Converting message into a grid
    arr = [[0] * len(key) for i in range(num_of_rows)]

    # decipher
    plain_text = ""
    k = 0
    itr = 0

    # print(arr[6][4])
    # itr = len(msg)

    for i in range(len(msg)):
        d = 0
        if k == len(key):
            k = 0
        else:
            d: int = int(num_loc[k])
        for j in range(num_of_rows):
            arr[j][d] = msg[itr]
            # print("j: {} d: {} m: {} l: {} ". format(j, d, msg[l], l))
            itr += 1
        if itr == len(msg):
            break
        k += 1
    print()

    for i in range(num_of_rows):
        for j in range(len(key)):
            plain_text += str(arr[i][j])
        # for
    # for

    print("\n\n========== Cesar encription ==========\n\n")
    print(plain_text)

    return plain_text

def cesar_decryption(final_encryption):

    encrypted_text = final_encryption.replace(",", " ")

    # Alphabet
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
    
    # Scroll key
    key = int (input("\n---------- Cesar's key: "))

    if key > 0 and key <= 37:
        # Decrypted text variable
        decrypted_text = ""
        
        # Cesar Decrypt method
        for et in encrypted_text:
            if et in alphabet:
                    decrypted_text += alphabet[((alphabet.index(et) - key) % (len(alphabet)))]
            else:
                if et == " ":
                    decrypted_text += et
                else:
                    decrypted_text += ""

        print("\n\n========== Plain text decrypted ==========\n\n")
        print(decrypted_text)
        
        return decrypted_text
        
    else:
        print("Key out of range")

def main():
    # Read file
    txtFile = open('message_encrypt.txt','r', encoding="utf8")
    fileContent = txtFile.readlines()
    txtFile.close()

    # Replace returns by spaces
    encrypted_text = ""
    for fc in fileContent:
        encrypted_text += fc

    # Print the encrypted text
    print("\n\n========== Encrypted text (transposition) ==========\n\n")
    print(encrypted_text)

    # Run transposition decryption
    to_cesar = transposition_decryption(encrypted_text)
    
    # Run cesar decryption
    final_result = cesar_decryption(to_cesar)
    
    # Create message_decrypt.txt file
    outputFile = open('message_decrypted.txt','w')
    outputFile.write(final_result)
    outputFile.close()
    print("\n\n========== Check message_decrypt.txt file ==========\n\n") 

if __name__ == "__main__":
    main()



