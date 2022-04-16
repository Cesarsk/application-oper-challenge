def to_complement(digit, base):
    return abs(digit - base)


def transform(value):
    chars = value.strip()

    reversed_string = ""
    for c in chars:
        if c.isdigit():
            reversed_string = str(to_complement(digit=int(c), base=9)) + reversed_string
        elif c.isupper():
            reversed_string = c.lower() + reversed_string
        elif c.islower():
            reversed_string = c.upper() + reversed_string
        else:
            reversed_string = c + reversed_string

    return reversed_string


if __name__ == '__main__':
    value = "FOoBar25$asdCOJN!120381203781"
    result = transform(value)
    print(result)

# todo small test case to make sure that the example provided is treated correclty by the application logic
