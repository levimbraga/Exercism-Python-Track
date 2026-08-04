def square_of_sum(number):
    """Returns the square of the sum of the first n numbers.
    
    Parameters:
        number(int): The number to sum the first n numbers.
        
    Returns:
        int: Square of the sum."""
    
 
    result = sum(range(1, number + 1)) ** 2
    return result


def sum_of_squares(number):
    """Returns the sum of the squares of the first n numbers.
        
    Parameters:
        number(int): The number to square the first n numbers.
            
    Returns:
        int: Sum of the squares."""

    result = 0
    for i in range(1, number + 1):
        result += (i ** 2)
    return result

def difference_of_squares(number):
    """Difference between the square of the sum of the first n natural numbers and the sum of the squares of the first n natural numbers.
            
    Parameters:
        number(int): The number to calculate de difference.
                
    Returns:
        int: The difference calculated."""


    result = square_of_sum(number) - sum_of_squares(number)
    return result
