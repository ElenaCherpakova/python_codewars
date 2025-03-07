# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

# Example 1:
# a1 = ["arp", "live", "strong"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []

# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
# In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
# Beware: In some languages r must be without duplicates.

# def in_array(array1, array2):
#     res = set()
#     for word_one in array1:
#         for word_two in array2:
#             if word_one in word_two:
#                 res.add(word_one)
#     return sorted(res)

def in_array(array1, array2):
    full_str = ' '.join(array2)
    res = { word for word in array1 if word in full_str }
    return sorted(res)

a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]      

print(in_array(a1, a2)) # ["arp", "live", "strong"]
