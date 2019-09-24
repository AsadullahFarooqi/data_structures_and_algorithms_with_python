def brute_force(n):
    if n <= 2:
        return 1
    return brute_force(n-1) + brute_force(n-2)

def dp_recursiv(n):
    d = {}
    if n in d:
        return d[n]
    if n <= 2:
        return 1
    
    d[n] = dp_recursiv(n-1) + dp_recursiv(n-2)
    return d[n]


def dp_bottom_up_iterative(n):
    d = {}
    for i in range(1, n+1):
        if i <= 2:
            d[i] = 1
            continue
        d[i] = d[i-1] + d[i-2]

    return d[n]

if __name__ == '__main__':
    n = 35
    print(dp_bottom_up_iterative(n))
    print(dp_recursiv(n))
    print(brute_force(n))