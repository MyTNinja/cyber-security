print('1. Encryption \n2. Decryption')
opt = int(input('\nEnter Choice: '))

key = int(input('\nEnter Key (default 3): ') or 3)

if opt == 1:
    plain_text = input('Enter Plain Text: ')
    encrypted_text = ''.join([chr(ord(i) + key) for i in plain_text])
    print('\nCipher Text: ', encrypted_text)

elif opt == 2:
    cipher_text = input('Enter Cipher Text: ')
    decrypted_text = ''.join([chr(ord(i) - key) for i in cipher_text])
    print('\nPlain Text:', decrypted_text)

else:
    print('Wrong Option')
