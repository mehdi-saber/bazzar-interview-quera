def is_valid():
    c_stack = []
    inp = input()
    if inp.__sizeof__() <= 1:
        return False
    for el in inp:
        if el in ['{', '(', '[']:
            c_stack.append(el)
        else:
            if c_stack.__len__() <= 0:
                return False
            c = c_stack.pop()
            if not ((c == '{' and el == '}') or
                    (c == '(' and el == ')') or
                    (c == '[' and el == ']')):
                return False

    return len(c_stack) <= 0


print('Valid' if is_valid() else 'Invalid')