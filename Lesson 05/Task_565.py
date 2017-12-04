"""
Three words
"""


text = "He is 123 man tests tests "
words = text.split()

words_counter = 0
result = False

for word in words:
    if word.isalpha():
        words_counter += 1
        if words_counter >=3:
            result = True
            break
    else:
        words_counter = 0
    
print(f'{text}, результат: {result}')