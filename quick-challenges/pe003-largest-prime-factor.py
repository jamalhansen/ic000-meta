# Largest prime factor from: https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
from math import ceil, sqrt

# We only need to check for primes up to the squareroot of the highest number
high_range = 600851475143
upper = int(ceil(sqrt(high_range)))
largest_prime = 2

def is_prime(number):
    if number % 2 == 0:
        return False

    prime = True
    y = 2

    while y < number and prime:
        if number % y == 0:
            prime = False
        y += 1

    return prime

# Find all prime numbers up to the upper limit and add them to a list
for x in range(upper, 3, -1):
    # first check to see if it is a factor
    print "Checking %d" % x

    if high_range % x == 0:
        # now check to see if it is prime
        if is_prime(x):
            print x
            break


