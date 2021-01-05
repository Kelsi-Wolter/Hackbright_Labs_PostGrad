"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    '''Returns list of even numbers in a list
        >>> get_all_evens([1, 2, 3, 4, 10, 20])
        [2, 4, 10, 20]

        >>> get_all_evens([1, 3, 5])
        []    
    '''
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums


def get_odd_indices(items):
    '''Returns list of items at odd-number indices from input list
        >>> get_odd_indices([1, 'hello', true, 500])
        ['hello', 500]
        >>> get_odd_indices(['k', 'e', 'l', 's', 'i'])
        ['e', 's']
    
    '''
    result = []

    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])
    
    return result


def print_as_numbered_list(items):
    '''Prints items in a list as a numbered list
    >>> print_as_numbered_list([1, 'hello', True])
    1. 1
    2. hello
    3. True
    
    '''
    list_num = 1

    for item in items:
        print(f'{list_num}. {item}')
        list_num += 1


def get_range(start, stop):
    '''Takes in two integers, returns list of integers within the range
    >>> get_range(0, 5)
    [0, 1, 2, 3, 4]
    
    '''
    nums = []

    for num in range(start, stop):
        nums.append(num)

    return nums


def censor_vowels(word):
    '''Replaces vowels in a string with asterisk
    >>> censor_vowels('hello world')
    'h*ll* w*rld'
    
    '''
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)
    
    return ''.join(chars)


def snake_to_camel(string):
    '''Change string from snake case to camel case
    >>> snake_to_camel('hello_world')
    'HelloWorld'
    >>> snake_to_camel('my_name_is_Kelsi')
    'MyNameIsKelsi'
    '''
    camel_case = []

    for word in string.split('_'):
        camel_case.append(f'{word[0].upper()}{word[1:]}')
    
    return ''.join(camel_case)


def longest_word_length(words):
    '''Takes in list of words, returns length of longest word in list
    >>> longest_word_length(['hey', 'programming', 'is', 'fun'])
    11
    
    '''

    longest = len(words[0])

    for word in words:
        if len(longest) < len(word):
            longest = len(word)

    return longest


def truncate(string):
    '''Truncates repeating characters into one character
    >>> truncate('yoooooooooo iiiiit issss 1999999991')
    'yo it is 191'
    
    '''
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) - 1]:
            result.append(char)

    return ''.join(result)


def has_balanced_parens(string):
    '''Counts parentheses in string and returns True if they are balanced
    >>> has_balanced_parens('((This) (is) (good))')
    True
    >>> has_balanced_parens('(Oh no!)(')
    False
    '''
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
            if parens < 0:
                return false

    return parens == 0 


def compress(string):
    '''Compresses words within a string with numbers to represent 
    repeating letters

    >>> compress('yellow fellow fiddles swimming too')
    'yel2ow fel2ow fid2les swim2ing to2'
    >>> compress('abc')
    'abc'
    '''
    compressed = []

    curr_char = ''
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
            
            if char_count > 1:
                compressed.append(str(char_count))
            curr_char = char
            char_count = 0
        char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))
        
    return ''.join(compressed)
