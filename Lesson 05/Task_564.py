"""
Secret message
"""

message = r'How are you? Eh, ok. Low or Lower? Ohhh.'
secret_message = ''

for charapter in message:
    if charapter.isupper():
        secret_message += charapter
print(secret_message)
