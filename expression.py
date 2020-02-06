import re


def math():
    in_str = input()
    # in_str = "(2+3)*((7+12)+(3*(1+2)))"
    tokenizer = re.compile(r'(\d+|[*+]|\(|\))')
    expression = tokenizer.findall(in_str)
    postfix = []
    stack = []
    for token in expression:
        token: str
        if token.isdecimal():
            postfix.append(int(token))
        elif token in "+*":
            while True:
                stack.append(token)
                break
        elif token == '(':
            stack.append(token)
        elif token == ')':
            c_pop = stack.pop()

            while c_pop != '(':
                postfix.append(c_pop)
                c_pop = stack.pop()
    while not len(stack) <= 0:
        postfix.append(stack.pop())
    stack = []
    for token in postfix:
        if token in {"*", "+"}:
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            result = eval(str(operand_1) + token + str(operand_2))
            stack.append(result)
        elif type(token) is int:
            stack.append(token)
    return stack[0]


if __name__ == '__main__':
    print(math())