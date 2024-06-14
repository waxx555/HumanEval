from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    count = 0
    max_count = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            count += 1
            max_count = max(max_count, count)
        elif paren_string[i] == ')':
            count -= 1
        if paren_string[i] == ' ':
            result.append(max_count)
            max_count = 0
    result.append(max_count)
    return result



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]
check(parse_nested_parens)