"""
PALINDROME CHECKER

This program checks if a given string is a palindrome.

Features:
    - Ignores punctuation, spaces, and capitalization.
    - Provides informative feedback to the user.
    - Re-runs the check until the user decides to exit.
"""

import string


def clean_string(s):
    """
    Clean the input string by removing all punctuation and spaces,
    and converting it to lowercase.

    Args:
        s (str): The string to be cleaned.

    Returns:
        str: The cleaned string.
    """
    return ''.join(char for char in s if char not in string.punctuation).replace(" ", "").lower()


def is_palindrome(s):
    """
    Check if the cleaned string is a palindrome.

    Args:
        s (str): The cleaned string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]


def main():
    """
    Main function to run the palindrome checker.
    """
    while True:
        user_input = input("\nEnter a string to check for palindrome (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting the Palindrome Checker. Goodbye!")
            break

        cleaned_input = clean_string(user_input)
        if is_palindrome(cleaned_input):
            print("Congrats, it's a palindrome!")
        else:
            print("Sorry, it's not a palindrome.")


if __name__ == "__main__":
    main()
