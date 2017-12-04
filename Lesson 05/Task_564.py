"""
Secret message
"""

message = r'How are you? Eh, ok. Low or Lower? Ohhh.'
secret_message = ''

for chapter in message:
    if chapter.isupper():
        secret_message += chapter
print(secret_message)
