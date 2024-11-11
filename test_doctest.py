"""
>>> add(0,2)
2
"""
def add(a, b) -> int:
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()