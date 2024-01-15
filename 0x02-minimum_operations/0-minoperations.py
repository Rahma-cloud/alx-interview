def minOperations(n):
    if n <= 1:
        return 0

    # Initialize an array to store the minimum operations for each number
    min_ops = [float('inf')] * (n + 1)
    min_ops[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                min_ops[i] = min(min_ops[i], min_ops[j] + i // j)
    return min_ops[n] if min_ops[n] != float('inf') else 0
