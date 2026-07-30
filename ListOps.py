"""Reimplementation of common list operations without using the builtins."""


def append(list1, list2):
    """Add all the items of list2 to the end of list1."""

    new_list = list1 + list2
    return new_list


def concat(lists):
    """Combine all the items of a series of lists into one flattened list."""

    new_list = []
    for item_list in lists:
        new_list = new_list + item_list

    return new_list


def filter(function, list):
    """Return the list of items for which the function returns True."""

    result_list = []
    for item in list:
        if function(item) == True:
            result_list.append(item)
    return result_list


def length(list):
    """Return the total number of items in the list."""

    size = 0
    for item in list:
        size += 1

    return size


def map(function, list):
    """Return the list of the results of applying the function to each item."""

    result_list = []
    for item in list:
        result_list.append(function(item))
    return result_list


def foldl(function, list, initial):
    """Fold the list into a single value, from the left."""

    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)

    return accumulator


def foldr(function, list, initial):
    """Fold the list into a single value, from the right."""

    accumulator = initial
    for item in reverse(list):
        accumulator = function(accumulator, item)

    return accumulator


def reverse(list):
    """Return the list with its items in the opposite order."""

    reverse_list = []

    for item in list:
        reverse_list.insert(0, item)
    return reverse_list
