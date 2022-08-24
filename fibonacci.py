def sumFibonacciSequence(nth=50):

    n1, n2 = 0, 1
    count = 0
    seq = []

    while count < nth:
        seq.append(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count += 1

    return f'Sum is {sum(seq)}'

print()
print(sumFibonacciSequence())
print()