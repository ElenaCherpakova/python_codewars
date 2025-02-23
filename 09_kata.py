# Your code will show Full name of the neighbor and the truncated version of the name as an array. If the number of the characters in name is less than or equal to two, it will return an array containing only the name as is.

def who_is_paying(name):
    if len(name) <= 2:
        return [name]
    return [name, name[:2]]



print(who_is_paying("Mexico"),["Mexico", "Me"])
print(who_is_paying("Melania"),["Melania", "Me"])
print(who_is_paying("Melissa"),["Melissa", "Me"])
print(who_is_paying("Me"),["Me"])
print(who_is_paying(""), [""])
print(who_is_paying("I"), ["I"])