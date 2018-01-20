"""
Cipher
"""

def rotate_plus90(grille):
    grille_90 = zip(*grille[::-1])
    grille_as_string = [''.join(row) for row in grille_90]
    return grille_as_string

def decrypt(crypted_text, cipher_grille):
    decrypted_text = ''
    for i in range(4):
        crypted_row = ''
        cipher_row = ''
        crypted_row = crypted_row.join(crypted_text)
        cipher_row  = cipher_row.join(cipher_grille)
        zipped_row = zip(cipher_row, crypted_row)
        part_clear_text = (text_cell for cipher_cell, text_cell in zipped_row if cipher_cell == 'X')
        decrypted_text += ''.join(part_clear_text)
        cipher_grille = rotate_plus90(cipher_grille)
    return decrypted_text

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