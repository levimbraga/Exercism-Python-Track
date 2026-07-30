"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    Parameters:
        word (str): The root word.

    Returns:
        str: Root word prepended with 'un'.
    """

    prefix_un = "un" + word
    return prefix_un


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    Parameters:
        vocab_words (list): A prefix followed by the words to prefix.

    Returns:
        str: The prefix and prefixed words, separated by ' :: '.
    """

    prefix = vocab_words[0]
    prefix_word = f" :: {prefix}".join(vocab_words)

    return prefix_word


def remove_suffix_ness(word):
    """Remove the suffix 'ness' from the word while keeping spelling in mind.

    Parameters:
        word (str): A word ending in 'ness'.

    Returns:
        str: The root word without the 'ness' suffix.
    """

    root = word[:-4]
    if root[-1] == "i":
        root = root[:-1]
        root = root + 'y'
    return root


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The sentence containing the adjective.
        index (int): The index of the adjective within the sentence.

    Returns:
        str: The adjective turned into a verb.
    """

    sentence = sentence.split()
    verb = sentence[index]
    if verb[-1:] == '.' or verb[-1:] == '!' or verb[-1:] == '?':
        verb = verb[:-1] + 'en'
    else:
        verb = verb + 'en'

    return verb
