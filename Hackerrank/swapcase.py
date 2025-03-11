def swap_case(s):
    x = ""
    for ch in s:
        if ch.isupper():
            c = ch.lower()
        else:
            c = ch.upper()
        x = x+c
    return x

