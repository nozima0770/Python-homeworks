# Lesson 7 Homework
# Task 1

def is_prime(n):
    if n < 2:
        return False # 0 and 1 are not prime numbers
    for i in range(2, int( n ** 0.5) + 1): # Only check up to square root of n
        if n % i == 0:
            return False # n is divisible by i, so it's not prime
    return True # No divisors found, so n is prime

print(is_prime(4)) 
print(is_prime(7))

# Task 2

def digit_sum(k):
    total = 0
    while k > 0:
        digit = k % 10     # Get the last digit
        total += digit     # Add it to the total
        k = k // 10        # Remove the last digit
    return total


print(digit_sum(24))
print(digit_sum(502))

# Task 3

def powers_of_two(n):
    k = 1
    while 2 ** k <= n:
        print(2 ** k, end=" ")
        k += 1
        
powers_of_two(10)
powers_of_two(1)
powers_of_two(20)
