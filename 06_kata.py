# Implement a function which accepts 2 arguments: string and separator.

# The expected algorithm: split the string into words by spaces, split each word into separate characters and join them back with the specified separator, join all the resulting "words" back into a sentence with spaces.

# For example:

# splitAndMerge("My name is John", " ")  ==  "M y n a m e i s J o h n"
# splitAndMerge("My name is John", "-")  ==  "M-y n-a-m-e i-s J-o-h-n"
# splitAndMerge("Hello World!", ".")     ==  "H.e.l.l.o W.o.r.l.d.!"
# splitAndMerge("Hello World!", ",")     ==  "H,e,l,l,o W,o,r,l,d,!"
def split_and_merge(string_, separator):
    words = string_.split()
    return ' '.join([separator.join(word) for word in words])
     

print(split_and_merge("My name is John"," ")) #"M y n a m e i s J o h n")
print(split_and_merge("My name is John","-")) #"M-y n-a-m-e i-s J-o-h-n")
print(split_and_merge("Hello World!",".")) #"H.e.l.l.o W.o.r.l.d.!")
print(split_and_merge("Hello World!",",")) # "H,e,l,l,o W,o,r,l,d,!")