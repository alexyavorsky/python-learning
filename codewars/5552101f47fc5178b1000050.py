def dig_pow(n, p):
    # your code
    t = [int(i) for i in str(n)]
    sum = 0
    for i in t:
        sum += i**p
        p += 1
    return sum // n if sum % n == 0 else -1
