def caesar_encrypt():
    print()
    print('Caesar Encryption')
    print()

    cipher = ''
    
    plain = input('Enter the plain text: ')
    key = int(input('Enter the key value (1~25): '))

    for i in plain:
        if 'A' <= i <= 'Z':
            cipher += chr((ord(i) + key - ord('A')) % 26 + ord('A'))
        elif 'a' <= i <= 'z':
            cipher += chr((ord(i) + key - ord('a')) % 26 + ord('a'))
        else:
            cipher += ' '

    print('Encrypting...\n.\n.\n.')
    print('Encrypted text:', cipher)
    print()

    main()

def rf_encrypt():
    print('Rail-Fence Encryption')

def xor_encrypt():
    print()
    print('XOR Encryption')
    print()

    cipher = ''

    plain = input('Enter the plain text: ')
    key = int(input('Enter the key value (0~255): '))

    for i in plain:
        cipher += chr(ord(i) ^ key)

    print('Encrypting...\n.\n.\n.')
    print('Encrypted text:', cipher)
    print()

    main()

def sub_encrypt():
    print()
    print('Substitution Encryption')
    print()

    mapping = {'A': 'N', 'B': 'K', 'C': 'Y', 'D': 'G', 'E': 'J', 'F': 'S', 'G': 'D', 
               'H': 'U', 'I': 'L', 'J': 'E', 'K': 'B', 'L': 'I', 'M': 'X', 'N': 'A', 
               'O': 'P', 'P': 'O', 'Q': 'W', 'R': 'V', 'S': 'F', 'T': 'Z', 'U': 'H', 
               'V': 'R', 'W': 'Q', 'X': 'M', 'Y': 'C', 'Z': 'T'}
    
    cipher = ''

    plain = input('Enter the plain text: ')

    for i in plain:
        if 'A' <= i <= 'Z':
            cipher += mapping[i]
        elif 'a' <= i <= 'z':
            cipher += mapping[i.upper()].lower()
        else:
            cipher += ' '
    
    print('Encrypting...\n.\n.\n.')
    print('Encrypted text:', cipher)
    print()

    main()

def morse_encrypt():
    print()
    print('Morse Code Encryption')
    print()

    morse_code = {'A': '·-', 'B': '-···', 'C': '-·-·', 'D': '-··', 'E': '·', 'F': '··-·', 'G': '--·', 
                  'H': '····', 'I': '··', 'J': '·---', 'K': '-·-', 'L': '·-··', 'M': '--', 'N': '-·', 
                  'O': '---', 'P': '·--·', 'Q': '--·-', 'R': '·-·', 'S': '···', 'T': '-', 'U': '··-', 
                  'V': '···-', 'W': '·--', 'X': '-··-', 'Y': '-·--', 'Z': '--··'}
    
    cipher = ''

    plain = input('Enter the plain text: ')

    for i in plain.upper():
        if 'A' <= i <= 'Z':
            cipher += morse_code[i] + ' '
        else:
            cipher += '   '
    
    print('Encrypting...\n.\n.\n.')
    print('Encrypted text:', cipher)
    print()

    main()

def caesar_decrypt():
    print()
    print('Caesar Decryption')
    print()

    plain = ''
    
    cipher = input('Enter the cipher text: ')
    key = int(input('Enter the key value (1~25): '))

    for i in cipher:
        if 'A' <= i <= 'Z':
            plain += chr((ord(i) - key - ord('A')) % 26 + ord('A'))
        elif 'a' <= i <= 'z':
            plain += chr((ord(i) - key - ord('a')) % 26 + ord('a'))
        else:
            plain += ' '

    print('Decrypting...\n.\n.\n.')
    print('Decrypted text:', plain)
    print()

    main()

def rf_decrypt():
    print('Rail-Fence Decryption')

def xor_decrypt():
    print()
    print('XOR Decryption')
    print()

    plain = ''

    cipher = input('Enter the cipher text: ')
    key = int(input('Enter the key value (0~255): '))

    for i in cipher:
        plain += chr(ord(i) ^ key)

    print('Decrypting...\n.\n.\n.')
    print('Decrypted text:', plain)
    print()
    main()

def sub_decrypt():
    print()
    print('Substitution Decryption')
    print()

    mapping = {'A': 'N', 'B': 'K', 'C': 'Y', 'D': 'G', 'E': 'J', 'F': 'S', 'G': 'D', 
               'H': 'U', 'I': 'L', 'J': 'E', 'K': 'B', 'L': 'I', 'M': 'X', 'N': 'A', 
               'O': 'P', 'P': 'O', 'Q': 'W', 'R': 'V', 'S': 'F', 'T': 'Z', 'U': 'H', 
               'V': 'R', 'W': 'Q', 'X': 'M', 'Y': 'C', 'Z': 'T'}
    
    plain = ''

    cipher = input('Enter the plain text: ')

    for i in cipher:
        if 'A' <= i <= 'Z':
            plain += mapping[i]
        elif 'a' <= i <= 'z':
            plain += mapping[i.upper()].lower()
        else:
            plain += ' '
    
    print('Decrypting...\n.\n.\n.')
    print('Decrypted text:', plain)
    print()

    main()

def morse_decrypt():
    print()
    print('Morse Code Decryption')
    print()

    morse_code = {'A': '·-', 'B': '-···', 'C': '-·-·', 'D': '-··', 'E': '·', 'F': '··-·', 'G': '--·', 
                  'H': '····', 'I': '··', 'J': '·---', 'K': '-·-', 'L': '·-··', 'M': '--', 'N': '-·', 
                  'O': '---', 'P': '·--·', 'Q': '--·-', 'R': '·-·', 'S': '···', 'T': '-', 'U': '··-', 
                  'V': '···-', 'W': '·--', 'X': '-··-', 'Y': '-·--', 'Z': '--··'}
    
    morse_code_for_decrypt = {v: k for k, v in morse_code.items()}
    
    plain = ''

    cipher = input('Enter the plain text: ')

    words = cipher.strip().split('   ')

    for word in words:
        letters = word.strip().split(' ')
        for i in letters:
            plain += morse_code_for_decrypt.get(i)
        plain += ' '
    
    print('Encrypting...\n.\n.\n.')
    print('Encrypted text:', plain.strip())
    print()

    main()

def main():
    while True:
        option = input('Would you like to encrypt or decrypt? ')
        
        if option.lower().strip() == 'encrypt' or option.lower().strip() == 'decrypt':
            break
        else:
            print('Invalid input. Please enter \'encrypt\' or \'decrypt\'. ')

    if option.lower().strip() == 'encrypt':
        while True:
            encrypt_type = int(input('\nWhich cipher are you using? \n1. Caesar Cipher \n2. Rail Fence Cipher \n3. XOR Cipher \n4. Substitution Cipher \n5. Morse Code \n'))

            if encrypt_type in [1, 2, 3, 4, 5]:
                break
            else:
                print('Invalid input. Please enter a number between 1~5. ')

        if encrypt_type == 1:
            caesar_encrypt()
        elif encrypt_type == 2:
            rf_encrypt()
        elif encrypt_type == 3:
            xor_encrypt()
        elif encrypt_type == 4:
            sub_encrypt()
        elif encrypt_type == 5:
            morse_encrypt()

    if option.lower().strip() == 'decrypt':
        while True:
            decrypt_type = int(input('Which cipher are you using? \n1. Caesar Cipher \n2. Rail Fence Cipher \n3. XOR Cipher \n4. Substitution Cipher \n5. Morse Code \n'))

            if decrypt_type in [1, 2, 3, 4, 5]:
                break
            else:
                print('Invalid input. Please enter a number between 1~5. ')

        if decrypt_type == 1:
            caesar_decrypt()
        elif decrypt_type == 2:
            rf_decrypt()
        elif decrypt_type == 3:
            xor_decrypt()
        elif decrypt_type == 4:
            sub_decrypt()
        elif decrypt_type == 5:
            morse_decrypt()

print()
print('-' * 10)
print('| Cipher |')
print('-' * 10)
print()

main()

print()