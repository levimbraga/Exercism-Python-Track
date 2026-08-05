def sum_of_multiples(level, multiples):
    unique_numbers = set()
    for multiple in multiples:
        if multiple == 0:
            continue
        else:
            limit = 0
            while (limit + multiple) < level:
                limit += multiple
                unique_numbers.add(limit)
            
    return sum(unique_numbers)

