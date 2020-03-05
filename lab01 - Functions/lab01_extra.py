"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    else:
        fact_list = []
        fact_list.append(n)
        while len(fact_list) < k:
            n = n - 1
            fact_list.append(n)
        product = 1
        for x in fact_list:
            product *= x
        return product

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    digit = []
    q = n // 10
    r = n % 10
    digit.append(r)
    while q > 10:
        r = q % 10
        digit.append(r)
        q = q // 10
    digit.append(q)
    k=0
    while k < len(digit)-1:
        if digit[k] == digit[k+1]:
            return True
        k = k + 1
    return False
