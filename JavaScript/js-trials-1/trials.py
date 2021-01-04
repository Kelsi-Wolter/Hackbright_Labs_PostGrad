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
    pass  # TODO: replace this line with your code


def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
