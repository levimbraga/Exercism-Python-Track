"""Reverse a string without relying on slicing tricks."""


def reverse(text):
    """Reverse the given text.

    Parameters:
        text (str): The text to reverse.

    Returns:
        str: The text, reversed.
    """

    text_list = []

    for letter in text:
        text_list.append(letter)

    text_list.reverse()

    reverse_text = ""

    for letter in text_list:
        reverse_text = reverse_text + letter

    return reverse_text
