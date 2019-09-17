def unique_in_order(iterable):
    current_char = None
    unique_chars = []
    for i in range(len(iterable)):
        eachChar = iterable[i]
        if eachChar != current_char:
            unique_chars.append(eachChar)
            current_char = eachChar
    return unique_chars
