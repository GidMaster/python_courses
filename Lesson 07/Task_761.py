"""
words and letters popularity
"""
import re

text = "hello, word of word"

chars_popularity = {}
words_popularity = {}

vocabulary = re.split(' |\.|, |\n', text)

for word in vocabulary:
    if word not in words_popularity.keys():
        words_popularity[word] = 0
    words_popularity[word] += 1
    for character in word:
        if character not in chars_popularity.keys():
            chars_popularity[character] = 0
        chars_popularity[character] += 1        

print(vocabulary)
print(words_popularity)
print(chars_popularity)