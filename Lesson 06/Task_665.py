"""
Lined words
"""

def checker(charapter):
    
    """
    Check procedure
    """
        
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')
    
    if charapter in vowels:
        state = 'vowel'
    elif charapter in consonants:
        state = 'consonant'
    else:
        state = 'not alfa'
    return state


def liner(word):
    previous_character = ''
    word = word.lower()
    if len(word) > 1:
        for character in word:
            #define state
            previous_state = checker(previous_character)
            current_state = checker(character)
            if current_state != previous_state:
                previous_character = character
                continue
            else:
                return 0
        return 1
    else:
        return 0

text = "A quantity of striped words."

vocabulary = text.split()

counter_word = 0

for word in vocabulary:
    counter_word += liner(word)
print(f'Number of striped words is {counter_word}')
