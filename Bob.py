def response(hey_bob):
    hey_bob = hey_bob.strip()

    if hey_bob == '':
        bob_response = 'Fine. Be that way!'

    elif hey_bob[-1] == '?':
        if hey_bob != hey_bob.upper():
            bob_response = 'Sure.'
        elif hey_bob == hey_bob.upper():
            has_letter = False
            for letter in hey_bob:
                if letter.isalpha():
                    has_letter = True
                    break
            if has_letter:
                bob_response = "Calm down, I know what I'm doing!"
            else:
                bob_response = 'Sure.'

    elif hey_bob == hey_bob.upper():
        has_letter = False
        for letter in hey_bob:
            if letter.isalpha():
                has_letter = True
                break
        if has_letter:
            bob_response = 'Whoa, chill out!'
        else:
            bob_response = 'Whatever.'
            
    else:
        bob_response = 'Whatever.'

    return bob_response
