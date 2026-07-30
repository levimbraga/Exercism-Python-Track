"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    Parameters:
        express_queue (list): The names in the express queue.
        normal_queue (list): The names in the normal queue.
        ticket_type (int): 1 for express, 0 for normal.
        person_name (str): The name of the person to add.

    Returns:
        list: The queue the person was added to.
    """

    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    elif ticket_type == 0:
        normal_queue.append(person_name)
        return normal_queue


def find_my_friend(queue, friend_name):
    """Search the queue for a name and return their queue position (index).

    Parameters:
        queue (list): The names in the queue.
        friend_name (str): The name to search for.

    Returns:
        int: The index of the friend in the queue.
    """

    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    """Insert a person at a specific index in the queue.

    Parameters:
        queue (list): The names in the queue.
        index (int): Where the person should be inserted.
        person_name (str): The name of the person to add.

    Returns:
        list: The queue with the person inserted.
    """

    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """Remove a person from the queue.

    Parameters:
        queue (list): The names in the queue.
        person_name (str): The name of the person to remove.

    Returns:
        list: The queue without the removed person.
    """

    queue.remove(person_name)
    return queue


def how_many_namefellows(queue, person_name):
    """Count how many times a name appears in the queue.

    Parameters:
        queue (list): The names in the queue.
        person_name (str): The name to count.

    Returns:
        int: How many times the name appears.
    """

    return queue.count(person_name)


def remove_the_last_person(queue):
    """Remove the last person from the queue and return their name.

    Parameters:
        queue (list): The names in the queue.

    Returns:
        str: The name of the person who was removed.
    """

    last_person = queue.pop()
    return last_person


def sorted_names(queue):
    """Sort the names in the queue alphabetically.

    Parameters:
        queue (list): The names in the queue.

    Returns:
        list: The names sorted alphabetically.
    """

    return sorted(queue)
