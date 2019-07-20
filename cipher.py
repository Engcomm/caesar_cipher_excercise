from string import ascii_lowercase, ascii_uppercase


def caesar_cipher(s, k):

    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return 'A non ascii character was found in the provided string'

    if k <= 100:
        pass
    else:
        return 'A integer larger than 100 was provided (0 <= k <= 100)'

    result = ''

    for char in s:
        if char.isupper():
            result += ascii_uppercase[(ascii_uppercase.index(char) - k) % 26]
        elif char.islower():
            result += ascii_lowercase[(ascii_lowercase.index(char) - k) % 26]
        else:
            result += char

    return result


if __name__ == '__main__':

    res = caesar_cipher('Take a string and ENCRYPT it with the caesar_cipher function!!!(pytest used for tests)', 99)
    print(res)
