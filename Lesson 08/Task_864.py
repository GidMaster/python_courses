"""
Cipher
"""

import numpy


def rotator_plus90(grille):
    grille_90 = tuple(zip(*grille[::-1]))

    return grille_90

def make_string(grille):
    pass


def decrypt(crypted_text, cipher_grille):
    cleartext = []
    for i in range(3):
        crypted_row = ''
        cipher_row = ''
        crypted_row = crypted_row.join(crypted_text)
        cipher_row  = cipher_row.join(cipher_grille)
        zipped_row = tuple(zip(cipher_row, crypted_row))
        part_clear_text = [element[1] for element in zipped_row if element[0] is 'X' ]
        cleartext.append(part_clear_text)
        cipher_grille = rotator_plus90(cipher_grille)
    return cleartext

def main():
    cipher_grille = ('X...',
                    '..X.',
                    'X..X',
                    '....')
for row in cipher:
    print(row)

    crypted_text = ('itdf',
                    'gdce',
                    'aton',
                    'qrdi')
# результат: 'icantforgetiddqd'

    cipher_grille = rotator_plus90(cipher_grille)
    print(cipher_grille)
    
    #clear_text = decryptor(crypted_text, cipher_grille)
    #print(clear_text)

if __name__ == '__main__':
    main()