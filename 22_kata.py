# I've got a crazy mental illness. I dislike numbers a lot. But it's a little complicated: The number I'm afraid of depends on which day of the week it is... This is a concrete description of my mental illness:

# Monday --> 12

# Tuesday --> numbers greater than 95

# Wednesday --> 34

# Thursday --> 0

# Friday --> numbers divisible by 2

# Saturday --> 56

# Sunday --> 666 or -666

# Write a function which takes a string (day of the week) and an integer (number to be tested) so it tells the doctor if I'm afraid or not. (return a boolean)
def am_I_afraid(day, num):
    if day == 'Monday' and num == 12:
        return True
    elif day == 'Tuesday' and num > 95:
        return True
    elif day == 'Wednesday' and num == 34:
        return True
    elif day == 'Thursday' and num == 0:
        return True
    elif day == 'Friday' and num % 2 == 0:
        return True
    elif day == 'Saturday' and num == 56:
        return True
    elif day == 'Sunday' and abs(num) == 666:
        return True
    return False
print(am_I_afraid("Monday", 13), False)
print(am_I_afraid("Sunday", -666), True)
print(am_I_afraid("Tuesday", 2), False)