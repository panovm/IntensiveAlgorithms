def are_brackets_correct(string: str) -> bool:
    D = []
    for bracket in string:
        if bracket in ['(', '[', '{']:
            D.append(bracket)
        else:
            if len(D) == 0:
                return False
            last_opened = D.pop()
            if (last_opened == '(' and bracket != ')') \
               or (last_opened == '[' and bracket != ']') \
               or (last_opened == '{' and bracket != '}') :
                return False
    if len(D):
        return False
    return True


# https://leetcode.com/problems/valid-parentheses/
