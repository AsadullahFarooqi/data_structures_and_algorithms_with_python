def cut_rod(p, n):
    """
    Brute force approach to Rod cutting problem
    
    Args:
        p (dict): length and it's price 
        n (int): the length of rod to cut
    
    Returns:
        TYPE: Description
    """
    if n==0:
        return 0
    temp_price = float("-inf")
    for i in range(1, n+1):
        if i not in p:
            continue
        temp_price = max(temp_price, p[i]+cut_rod(p, n-i)) # finds the max in (p[i], r1 + rn-2, r2 + rn-2....., rn-1+r1)

    return temp_price

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]

    if n == 0:
        q = 0

    else:
        q = float("-inf")
        for i in range(1, n+1):
            if i not in p:
                continue
            q = max(q, p[i]+memoized_cut_rod_aux(p, n-i, r))
    r[n] = q
    return q 


def memoized_cut_rod(p, n):
    """
    dinamic approach to rod cutting problem
    
    Args:
        p (dict): length and it's price 
        n (int): the length of rod to cut
    """
    r = [float("-inf")] * (n+1)

    return memoized_cut_rod_aux(p, n, r)

def bottom_up_cut_rod(p, n):
    r = [0] * (n+1)

    for i in range(1, n+1):
        q = float("-inf")
        for j in range(1, i+1):
            if j not in p:
                continue
            q = max(q, p[j]+r[i-j])
        r[i] = q

    return r[n]

if __name__ == '__main__':
    price_dict = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}
    n = 108
    print(bottom_up_cut_rod(price_dict, n))
