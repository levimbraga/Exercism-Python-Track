"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase.

    Parameters:
        title (str): The title to capitalize.

    Returns:
        str: The title in title case.
    """

    return title.title()


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    Parameters:
        sentence (str): The sentence to check.

    Returns:
        bool: Does the sentence end with a punctuation mark?
    """

    if sentence.endswith('.') or sentence.endswith('!') or sentence.endswith('?'):
        return True
    else:
        return False


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    Parameters:
        sentence (str): The sentence to clean up.

    Returns:
        str: The sentence without leading or trailing whitespace.
    """

    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    Parameters:
        sentence (str): The sentence to edit.
        old_word (str): The word to replace.
        new_word (str): The replacement word.

    Returns:
        str: The sentence with the word replaced.
    """

    return sentence.replace(old_word, new_word)
