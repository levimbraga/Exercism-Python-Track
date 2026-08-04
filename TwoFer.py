def two_fer(name='you'):
    """Determine what you will say as you give away the extra cookie
    
    Parameters:
        name(str): The name of the person

    Returns:
        str: What you will say to the person
    """
    name = name.strip()
    
    dialogue = f'One for {name}, one for me.'
    
    return dialogue

