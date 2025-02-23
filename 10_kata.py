# In this kata you will create a function that takes in a list and returns a list with the reverse order.

# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]

def reverse_list(l):
    return l[::-1]
# or
# def reverse_list(l):
#     return l.reverse()

print(reverse_list([1,2,3,4]), [4,3,2,1])
print(reverse_list([3,1,5,4]), [4,5,1,3])
print(reverse_list([3,6,9,2]), [2,9,6,3])
print(reverse_list([1]), [1])