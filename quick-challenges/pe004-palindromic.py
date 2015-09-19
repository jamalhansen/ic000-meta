def is_palendrome(number):
    val = str(number)
    if val == val[::-1]:
        print number
        return True
    return False

def check(x, y):
    prod = x * y
    print "Checking %d * %d" % (x, y)
    return is_palendrome(prod)

solution_one = 0
solution_two = 0

found = False
first = 999
second = 999

while not found:
    found = check(first, second)
    if found:
        solution_one = first * second

    first -= 1

found = False
first = 999
second = 999

while not found:
    found = check(first, second)
    if found:
        solution_two = first * second

    first -= 1
    second -= 1

print solution_one, solution_two
