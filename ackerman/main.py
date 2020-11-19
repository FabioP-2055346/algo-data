def ackermann_recursive(m, n, s="%s"):
    print(s % ("A(%d,%d)" % (m, n)))
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann_recursive(m - 1, 1, s)
    n2 = ackermann_recursive(m, n - 1, s % ("A(%d,%%s)" % (m - 1)))
    return ackermann_recursive(m - 1, n2, s)


def ackermann_iterative(m, n):
    stack = [m]
    while stack:
        m = stack.pop()
        if m == 0:
            n = n + 1
        elif n == 0:
            n = 1
            stack.append(m - 1)
        else:
            stack.append(m - 1)
            n = n - 1
            stack.append(m)
    return n


if __name__ == "__main__":
    r = ackermann_iterative(2, 2)
    print("Result:", r)
    print(ackermann_recursive(2, 2))
