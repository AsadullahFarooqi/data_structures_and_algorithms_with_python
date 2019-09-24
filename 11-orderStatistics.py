import random

def partition(array, start, end):
    x = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[end] = array[end], array[i+1]
    return i

def randomized_partition(array, start, end):
    random_var = random.randrange(start, end+1)
    array[random_var], array[end] = array[end], array[random_var]
    return partition(array, start, end)

def randomized_select(array, start, end, i):
    if start == end:
        return array[start]

    povit = randomized_partition(array, start, end)
    k = povit - start+1
    if i == k:
        return array[povit]
    elif i < k:
        return randomized_select(array, start, povit, i)
    else:
        return randomized_select(array, povit+1, end, i-k)

if __name__ == '__main__':
    # list_ = [1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297,1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,1709,1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,1811,1823,1831,1847,1861,1867,1871,1873,1877,1879,1889,1901,1907,1913,1931,1933,1949,1951,1973,1979,1987,1993,1997,1999,2003,2011,2017,2027,2029,2039,2053,2063,2069]
    # list_ = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    list_ = [489, 1709, 1103, 1307, 1669, 1499, 1069, 63, 1459, 1019]
    print(randomized_select(list_, 0, len(list_)-1, 2))