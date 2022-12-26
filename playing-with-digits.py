def dig_pow(n, p):
    
    dig_list = list(map(lambda n: int(n), list(str(n))))

    def pow(num, i):
        res = 0
        for j in num:
            res = res + j**(i)
            i = i + 1
        return res
    
    if not((pow(dig_list, p))/n)%1 == 0:
        return -1
    return pow(dig_list, p)/n


# with deconstructing
def dig_pow1(n, p):
    t = sum( int(d) ** (p+i) for i, d in enumerate(str(n)) )
    return t//n if t%n==0 else -1

print(dig_pow1(89, 1))