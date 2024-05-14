plain_text = 'ACT'

# plain text to equivalent matrix
pt_matrix = [[0] for i in range(3)]
for i in range(3):
    pt_matrix[i][0] += ord(plain_text[i]) % 65

# print(pt_matrix)

key = 'GYBNQKURP'

# key to equivalent matrix
key_matrix = [[0] * 3 for i in range(3)]
k = 0
for i in range(3):
    for j in range(3):
        key_matrix[i][j] += ord(key[k]) % 65
        k = k + 1

# print(key_matrix)

# matrix multiplication
res = [[sum(a * b for a, b in zip(krow, ptcol)) % 26 for ptcol in zip(*pt_matrix)] for krow in key_matrix]

# print(res)

# multiplication result to cipher text
cipher = []
for i in range(3):
    cipher.append(chr(res[i][0] + 65))

cipher_text = ''.join(i for i in cipher)

# result
print('Plain Text: ', plain_text)
print('Key: ', key)
print('Cipher Text: ', cipher_text)
