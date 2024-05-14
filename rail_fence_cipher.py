plain_text = input('Enter Plain Text: ')
key = input('Enter Key: ')

cols = len(plain_text)
rows = len(key)

encryption_space = [[' '] * cols for _ in range(rows)]

direction = 0
row_index = 0
for i in range(cols):
    encryption_space[row_index][i] = plain_text[i]
    if row_index == 0:
        direction = 0
    elif row_index == rows - 1:
        direction = 1
    if direction == 0:
        row_index += 1
    else:
        row_index -= 1

for i in range(rows):
    print("".join(encryption_space[i]))

cipher = []
for i in range(rows):
    for j in range(cols):
        if encryption_space[i][j] != ' ':
            cipher.append(encryption_space[i][j])

cipher_text = ''.join(cipher)
print('Cipher Text: ', cipher_text)
