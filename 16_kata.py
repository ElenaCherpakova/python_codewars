# Write a function to split a string and convert it into an array of words.

# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]

def string_to_array(s):
    return s.split() if s else ['']

print(string_to_array("Robin Singh")) #["Robin", "Singh"])
print(string_to_array("CodeWars")) #["CodeWars"])
print(string_to_array("I love arrays they are my favorite")) # ["I", "love", "arrays", "they", "are", "my", "favorite"])
print(string_to_array("1 2 3")) # ["1", "2", "3"])
print(string_to_array("")) # [""])