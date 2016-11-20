import fractions

def add_frac(frac1, frac2):         # frac1 + frac2
    frac3 = [0,0]
    M = frac1[-1]*frac2[-1]
    L = frac1[0]*frac2[-1]+frac2[0]*frac1[-1]
    gcd = fractions.gcd(L,M)
    frac3 = [L/gcd, M/gcd]
    return frac3


def sub_frac(frac1, frac2):        # frac1 - frac2
    sub = [-frac2[0], frac2[-1]]
    return add_frac(frac1,sub)

def mul_frac(frac1, frac2):        # frac1 * frac2
    frac3 = [0, 0]
    a = frac1[0]*frac2[0]
    b = frac1[-1]*frac2[-1]
    gcd = fractions.gcd(a, b)
    a /= gcd
    b /= gcd
    frac3[0] = a
    frac3[-1] = b
    return frac3

def div_frac(frac1, frac2):        # frac1 / frac2
    rev = [frac2[-1],frac2[0]]
    return mul_frac(frac1,rev)
def is_positive(frac):             # bool, czy dodatni
    if(frac[0]*frac[-1]>0):
        return True
    else:
        return False
def is_zero(frac):                 # bool, typu [0, x]
    if(frac[0]==0):
        return True
    else:
        return False
def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    cmp = sub_frac(frac1,frac2)
    if is_zero(cmp):
        return 0
    if is_positive(cmp):
        return 1
    else:
        return -1
def frac2float(frac):               # konwersja do float
    return float(frac[0]/frac[-1])


f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznaczność)
f5 = [0, 2]                   # zero (niejednoznaczność)

"""print(add_frac([2,4],[4,4]))
print(sub_frac([1,2],[1,3]))
print(mul_frac([3,4],[6,8]))
print(div_frac([3,4],[6,8]))
print(is_positive([3,4]))
print(is_zero([0,3]))
print(cmp_frac([1,2],[4,7]))
print(frac2float([1,3]))"""