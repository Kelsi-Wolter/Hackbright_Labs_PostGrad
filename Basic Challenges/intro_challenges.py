# Challenge 1: Find the Range

# Given a list of numbers, return the smallest and the largest number.

# We’ve given you range.py, which includes the stub of a find_range function:


def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple.
    
    >>> find_range([3, 4, 2, 5, 10])
    (2, 10)

    >>> find_range([43, 3, 44, 20, 2, 1, 100])
    (1, 100)

    >>> find_range([])
    (None, None)

    >>> find_range([7])
    (7, 7)
    
    """

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
# If the number is evenly divisible by both 3 and 5, say ‘fizzbuzz’. 
# Otherwise, say the number.

# We given you a file, fizzbuzz.py, with a method, fizzbuzz:

def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion.
    
    >>> fizzbuzz()
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    17
    fizz
    19
    buzz
    
    """
    for num in range(1, 21):
        if num % 3 == 0 and num % 5 == 0:
            print('fizzbuzz')
        elif num % 3 == 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        else:
            print(num)


# Challenge 3: Longest Word
# Write a function, find_longest_word, that takes a list of words and returns the length 
# of the longest one.

# We’ve given you longest-word.py, which includes the stub of a find_longest_word function:

def find_longest_word(words):
    """Return longest word in list of words.
    
    >>> find_longest_word(["hi", "hello"])
    'The longest word was hello, with a length of 5'

    >>> find_longest_word(["Balloonicorn", "Hackbright"])
    'The longest word was Balloonicorn, with a length of 12'

    """

    longest_len = 0
    longest_word = ''

    for word in words:
        word_len = len(word)
        if word_len > longest_len:
            longest_len = word_len
            longest_word = word
    
    return f'The longest word was {longest_word}, with a length of {longest_len}'


# Challenge 4: Decode

# In this challenge, you’ll write a decoder.

# A valid code is a sequence of numbers and letters, always starting with a number and 
# ending with letter(s).

# Each number tells you how many characters to skip before finding a good letter. 
# After each good letter should come the next next number.

# For example, the string “hey” could be encoded by “0h1ae2bcy”. This means “skip 0, 
# find the ‘h’, skip 1, find the ‘e’, skip 2, find the ‘y’”.

# A single letter should work

# We’ve provided a file, decode.py, with a stub function in it:

def decode(s):
    """Decode a string.
    
    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

    >>> decode("0h1ae2bcy")
    'hey'

    """

    start = 0
    word = []

    while start < len(s):
        step = int(s[start]) + 1
        char = s[start + step]

        word.append(char)

        start = start + step + 1
             
    return ''.join(word)

