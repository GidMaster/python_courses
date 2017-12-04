"""
Three words
"""
import re

text = "12 He is man 123"
three_words_pattern = re.compile(r'\D+ \D+ \D+')

if three_words_pattern.search(text):
    print(f'{text}, результат: True')
else:
    print(f'{text}, результат: False')