import sys

def encode(message, shift):
    result = []

    for char in message.upper():
        if 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))

    return ''.join(result)


shift = int(sys.argv[1])
message = sys.stdin.read()

encoded = encode(message, shift)

count = 0

for i in range(0, len(encoded), 5):
    print(encoded[i:i+5], end=' ')
    count += 1
    if count == 10:
        print()
        count = 0

if count != 0:
    print(import sys

def encode(message, shift):
    result = ""
    for char in message.upper():
        if char.isalpha():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    return result

shift = int(sys.argv[1])

message = ""
for line in sys.stdin:
    message += line

encoded = encode(message, shift)

count = 0
for i in range(0, len(encoded), 5):
    print(encoded[i:i+5], end=" ")
    count += 1
    if count % 10 == 0:
        print())
