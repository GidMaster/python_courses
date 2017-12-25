"""
words and letters popularity
"""
import re
from collections import Counter

text = "hello, word of word"

chars_popularity = {}


vocabulary = re.split(' |\.|, |\n', text)

word_popularity = dict(Counter(vocabulary))
chars_popularity
print(word_popularity)
