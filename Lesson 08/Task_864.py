"""
Cipher
"""

def rotate_plus90(grille):
    grille_90 = tuple(zip(*grille[::-1]))
    grille_as_string = tuple(''.join(row) for row in grille_90 )
    return grille_as_string

def decrypt(crypted_text, cipher_grille):
    cleartext = ''
    for i in range(4):
        crypted_row = ''
        cipher_row = ''
        crypted_row = crypted_row.join(crypted_text)
        cipher_row  = cipher_row.join(cipher_grille)
        zipped_row = tuple(zip(cipher_row, crypted_row))
        part_clear_text = (element[1] for element in zipped_row if element[0] is 'X')
        cleartext += ''.join(part_clear_text)
        cipher_grille = rotate_plus90(cipher_grille)
    return cleartext

def main():
    cipher_grille = ('X...',
                    '..X.',
                    'X..X',
                    '....')

    crypted_text = ('itdf',
                    'gdce',
                    'aton',
                    'qrdi')
    
    clear_text = decrypt(crypted_text, cipher_grille)
    print(clear_text)

if __name__ == '__main__':
    main()