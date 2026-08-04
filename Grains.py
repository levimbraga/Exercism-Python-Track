def square(number):
    if type(number) == int and 1 <= number <= 64:
        number_grains = 1
        if number != 1:
            number_grains = 2 ** (number - 1)

        return number_grains
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    total_grains = 0
    for i in range(64):
        total_grains = total_grains + (2 ** i)
    
    return total_grains

