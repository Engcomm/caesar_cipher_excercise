from myapp import caesar_cipher
from string import ascii_lowercase as alphabet

"""
python3 -m pytest -v
"""


def test_lowercase():
    assert caesar_cipher('abc', 0) == 'abc'
    assert caesar_cipher('abc', 1) == 'zab'
    assert caesar_cipher('abc', 2) == 'yza'


def test_uppercase():
    assert caesar_cipher('ABC', 0) == 'ABC'
    assert caesar_cipher('ABC', 1) == 'ZAB'
    assert caesar_cipher('ABC', 2) == 'YZA'


def test_mixed_case():
    assert caesar_cipher('AbC', 0) == 'AbC'
    assert caesar_cipher('aBc', 1) == 'zAb'
    assert caesar_cipher('abC', 2) == 'yzA'


def test_spaces():
    assert caesar_cipher('a b c', 0) == 'a b c'
    assert caesar_cipher(' abc ', 1) == ' zab '
    assert caesar_cipher('a bc ', 2) == 'y za '


def test_numbers():
    assert caesar_cipher('123', 0) == '123'
    assert caesar_cipher('123 abc', 1) == '123 zab'
    assert caesar_cipher('a1b2c3', 2) == 'y1z2a3'


def test_symbols():
    assert caesar_cipher('!@#$%^&*()_+', 0) == '!@#$%^&*()_+'
    assert caesar_cipher('!@#$%^&*()_+', 1) == '!@#$%^&*()_+'


def test_range():
    assert caesar_cipher('abc', 25) == 'bcd'
    assert caesar_cipher('abc', 26) == 'abc'
    assert caesar_cipher('abc', 27) == 'zab'

    for i in range(101):
        assert caesar_cipher('abc', i)

    assert caesar_cipher('abc', 200) == 'A integer larger than 100 was provided (0 <= k <= 100)'


def test_alphabet():
    assert caesar_cipher(alphabet, 0) == alphabet
    assert caesar_cipher(alphabet, 1) == alphabet[-1:] + alphabet[0: -1]
    assert caesar_cipher(alphabet, 2) == alphabet[-2:] + alphabet[0: -2]


def test_ascii():
    assert caesar_cipher('строка', 0) == 'A non ascii character was found in the provided string'
