"""
reverse dictionary
"""

book = {'Petr': '546810', 'Katya': '241815'}
reverse = dict(zip(book.values(), book.keys()))

print(reverse)