# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# def fake_bin(x):
#     nums = list(x)
#     res = ''
#     for num in nums:
#         if int(num) < 5:
#             res += '0'
#         else:
#             res += '1'
#     return res

# OR 

def fake_bin(x):
    return ''.join('0' if int(num) < 5 else '1' for num in x)


print(fake_bin("45385593107843568")) #"01011110001100111"
print(fake_bin("509321967506747")) #"101000111101101", 
