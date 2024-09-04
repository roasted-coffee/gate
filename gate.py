def NAND(a, b):
    """
    Return True(0) if either input are True(1) else False(0)
    """
    if a and b:
        return 0
    return 1


def NOT(a):
    """
    Return False(0) if a is True(1) else False(0)
    """
    return NAND(a, a)
