# When provided with a letter, return its position in the alphabet.

# Input :: "a"

# Output :: "Position of alphabet: 1"

# Note: Only lowercased English letters are tested


def position(letter):
    num = ord(letter.lower()) - ord('a') + 1
    return f'Position of alphabet: {num}'

print(position("a"), "Position of alphabet: 1")
print(position("z"), "Position of alphabet: 26")
print(position("e"), "Position of alphabet: 5")