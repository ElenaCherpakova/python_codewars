# Complete the function nato that takes a word in parameter and returns a string that spells the word using the NATO phonetic alphabet.

# There should be a space between each word in the returned string, and the first letter of each word should be capitalized.

# For those of you that don't want your fingers to bleed, this kata already has a dictionary typed out for you.

# Examples
# "hi"      -->  "Hotel India"
# "abc"     -->  "Alpha Bravo Charlie"
# "babble"  -->  "Bravo Alpha Bravo Bravo Lima Echo"
# "Banana"  -->  "Bravo Alpha November Alpha November Alpha"

def nato(word):
    nato_dict = {
        'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo', 
        'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliett', 
        'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November', 'o': 'Oscar', 
        'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango', 
        'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'X-ray', 'y': 'Yankee', 
        'z': 'Zulu'
    }
    # res = []
    # for char in word:
    #     res.append(nato_dict[char.lower()])
    # return " ".join(res)
    return " ".join(nato_dict[char.lower()] for char in word)


print(nato('HI'))
print(nato("abc")) # "Alpha Bravo Charlie"
print(nato("babble")) # "Bravo Alpha Bravo Bravo Lima Echo"
print(nato("Banana")) # "Bravo Alpha November Alpha November Alpha"