"""
A bunch of string or text based utilities.
"""


def count(string):
    """ Counts the number of characters in a given string. """
    return len(string)


def contains(text, string):
    """
    Returns true if some given text is in the given string,
    otherwise returns false.
    """
    return text in string
