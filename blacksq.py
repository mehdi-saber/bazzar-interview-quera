from collections import deque


def dp_search(params, memo, mat):
    s, e, j = params
    if s == e:
        return mat[s][j]
    if params in memo:
        return memo[params]

    result = dp_search((s + 1, e, j), memo, mat) and dp_search((s, e, j), memo, mat)
    memo[params] = result
    return result


def square_a(in_std):
    n, m = tuple(map(int, in_std.readline().split()))
    mat = []
    for i in range(n):
        line = in_std.readline().replace('\n', '')
        line = list(map(int, [*line]))
        line = list(map(bool, line))
        mat.append(line)
    memo = dict()
    for i in range(n - m):
        cols = deque()
        for j in range(n - m):
            new_col = dp_search((i, i + m - 1, j), memo, mat)
            cols.append(new_col)
            check = True
            if len(cols) >= m:
                for col in cols:
                    check &= col
                cols.popleft()
                if check:
                    return True

    return False


if __name__ == '__main__':
    # input_method = sys.stdin
    input_method = open("bsquare/2")

    if square_a(input_method):
        print('Yes')
    else:
        print('No')
