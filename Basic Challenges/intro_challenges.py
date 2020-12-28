# Challenge 1: Find the Range

# Given a list of numbers, return the smallest and the largest number.

# >>> find_range([3, 4, 2, 5, 10])
# (2, 10)

# >>> find_range([43, 3, 44, 20, 2, 1, 100])
# (1, 100)
# For an empty list, it should return None as both smallest and largest:

# >>> find_range([])
# (None, None)
# Make sure it works with a list of one item, which is both smallest and largest:

# >>> find_range([7])
# (7, 7)

# We’ve given you range.py, which includes the stub of a find_range function:


def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple."""

    if nums == []:
        nums_range = (None, None)
    else:
        nums_min = min(nums)
        nums_max = max(nums)

        nums_range = (nums_min, nums_max)

    return nums_range


# Challenge 2: FizzBuzz
# Write a program that counts from 1 to 20 in fizzbuzz fashion.
# To do so, loop from 1 to 20 (inclusive). Each time through, if the number is 
# evenly divisible by 3, say ‘fizz’. If the number is evenly divisible by 5, say ‘buzz’. 
# If the number is evenly divisible by both 3 and 5, say ‘fizzbuzz’. Otherwise, say the number.
# For example:
# >>> fizzbuzz()
# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz
# 11
# fizz
# 13
# 14
# fizzbuzz
# 16
# 17
# fizz
# 19
# buzz
# We given you a file, fizzbuzz.py, with a method, fizzbuzz:

def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion."""
    for num in range(1, 21):
        if num % 3 == 0 and num % 5 == 0:
            print('fizzbuzz')
        elif num % 3 == 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        else:
            print(num)