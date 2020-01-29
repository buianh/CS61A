"""Lab 1: Expressions and Control Structures"""

def both_positive(a, b):
    """Returns True if both a and b are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    if a > 0 and b > 0:
        return True
    else:
        return False # You can replace this line!

def sum_digits(x):
    """Sum all the digits of x.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    digit = []
    q = x // 10
    r = x % 10
    digit.append(r)
    while q > 10:
        r = q % 10
        digit.append(r)
        q = q // 10
    digit.append(q)
    return sum(digit)
