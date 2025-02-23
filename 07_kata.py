# Find the sum of all multiples of n below m

# Keep in Mind
# n and m are natural numbers (positive integers)
# m is excluded from the multiples

def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    return sum(range(n, m, n))


print(sum_mul(0, 0), 'INVALID')
print(sum_mul(2, 9), 20)
print(sum_mul(4, -7), 'INVALID')
print(sum_mul(4, 123), 1860)
print(sum_mul(123, 4567), 86469)