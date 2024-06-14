
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    if a == b:
        return None
    if type(a) == type(b):
        return max(a, b)
    if type(a) == int and type(b) == float:
        return b
    if type(a) == float and type(b) == int:
        return a
    if type(a) == str and type(b) == int:
        return a
    if type(a) == int and type(b) == str:
        return b
    if type(a) == str and type(b) == float:
        return b
    if type(a) == float and type(b) == str:
        return a
    
def check(candidate):

    # Check some simple cases
    assert candidate(1, 2) == 2
    assert candidate(1, 2.5) == 2.5
    assert candidate(2, 3) == 3
    assert candidate(5, 6) == 6
    assert candidate(1, "2,3") == "2,3"
    assert candidate("5,1", "6") == "6"
    assert candidate("1", "2") == "2"
    assert candidate("1", 1) == None

    # Check some edge cases that are easy to work out by hand.
    assert True

check(compare_one)