# basic_string_operations.py

def concatenate_strings(str1: str, str2: str) -> str:
    """
    Concatenates two strings.
    
    Args:
        str1 (str): The first string.
        str2 (str): The second string.
    
    Returns:
        str: The concatenation of str1 and str2.
    """
    return str1 + str2


def capitalize_string(string: str) -> str:
    """
    Capitalizes the first letter of the string.
    
    Args:
        string (str): The string to capitalize.
    
    Returns:
        str: The string with the first letter capitalized.
    """
    return string.capitalize()


def count_characters(string: str) -> int:
    """
    Counts the number of characters in a string.
    
    Args:
        string (str): The string to count characters in.
    
    Returns:
        int: The number of characters in the string.
    """
    return len(string)


def reverse_string(string: str) -> str:
    """
    Reverses the string.
    
    Args:
        string (str): The string to reverse.
    
    Returns:
        str: The reversed string.
    """
    return string[::-1]
