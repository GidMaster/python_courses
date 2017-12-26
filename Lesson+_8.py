cipher_grille = ('X...',
                '..X.',
                'X..X',
                '....')
crypted_text = ('itdf',
                'gdce',
                'aton',
                'qrdi')

grille = tuple(zip(*(cipher_grille, crypted_text)))
for row in grille:
    print(row)
    part_clear_text = tuple(element[1] for element in row if element[0] is 'X')
    print(part_clear_text)
print()
