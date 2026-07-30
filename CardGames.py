"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round and the two that follow it.
    """

    rounds = [number, number + 1, number + 2]
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The rounds played afterwards.

    Returns:
        list: All rounds played, in order.
    """

    rounds = rounds_1 + rounds_2
    return rounds


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number to look for.

    Returns:
        bool: Was the round played?
    """

    if number in rounds:
        return True
    else:
        return False


def card_average(hand):
    """Calculate and return the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average card value.
    """

    average = sum(hand) / len(hand)
    return average


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the actual average?
    """

    average = sum(hand) / len(hand)
    first_and_last = (hand[0] + hand[-1]) / 2
    median = len(hand) // 2
    median_number = hand[median]

    if median_number == average or first_and_last == average:
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the two averages equal?
    """

    even_indexed = hand[0::2]
    odd_indexed = hand[1::2]

    average_even = sum(even_indexed) / len(even_indexed)
    average_odd = sum(odd_indexed) / len(odd_indexed)

    if average_even == average_odd:
        return True
    else:
        return False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with the last Jack doubled, if there was one.
    """

    if hand[-1] == 11:
        hand = hand[:-1]
        hand.append(22)

    return hand
