def get_most_common_char(input_str):
    """
    Returns the most common letter (a-z) in the input string.
    :param input_str:
    :return:
    """

    ################################################################
    # Question 2
    # This function doesn't handle capitalized letters correctly (why not?).
    # Add some code here so that the function works as expected.
    # Hint: Check the Python string docs for some useful built-in functions that may help:
    # https://docs.python.org/3.1/library/string.html
    ################################################################
    # REPLACE THIS LINE WITH YOUR CODE
    ################################################################

    # define a dictionary mapping all letters a-z to their current counts, which start at 0
    char_counts = {chr(i): 0 for i in range(ord('a'), ord('z'))}

    # run through input string to get character counts
    for char in input_str:
        if char in char_counts:
            char_counts[char] = char_counts[char] + 1

    # get the character with the maximum count from the dictionary
    max_count = 0
    max_char = 'a'
    for char in char_counts.keys():
        if char_counts[char] > max_count:
            max_count = char_counts[char]
            max_char = char
    return max_char

if __name__ == "__main__":
    x = input("Enter a string:")
    while x:
        print("The most common letter in the string is " + get_most_common_char(x))
        x = input("Enter a string:")
