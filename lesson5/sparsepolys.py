
def add_poly(poly1, poly2):         # poly1(x) + poly2(x)
    poly3 = poly1.copy()
    for x in poly2:
        if x in poly3:
            poly3[x] += poly2[x]
        else:
            poly3[x] = poly2[x]
    return poly3

def sub_poly(poly1, poly2):        # poly1(x) - poly2(x)
    poly3 = poly1.copy()
    for x in poly2:
        if x in poly3:
            poly3[x] -= poly2[x]
        else:
            poly3[x] = -poly2[x]
    return poly3

def mul_poly(poly1, poly2):         # poly1(x) * poly2(x)
    polys = []
    poly3 = {}
    for a in poly1:
        pol = {}
        for b in poly2:
            pol.update({a+b:poly1[a]*poly2[b]})
        polys.append(pol)
    for prod in polys:
        poly3 = add_poly(poly3,prod)
    return poly3

def is_zero(poly):                  # bool, [0], [0,0], itp.
    if len(poly) == 1 and 0 in poly.values():
        return True
    else:
        return False
def cmp_poly(poly1, poly2):         # bool, porównywanie
    for a in poly1:
        if a not in poly2:
            return False
        if poly1[a] != poly2[a]:
            return False
    for b in poly2:
        if b not in poly1:
            return False
    return True

def eval_poly(poly, x0):           # poly(x0), algorytm Hornera
    power = max(poly.keys())
    coef = {}
    for i in range(power+1):
        if i in poly.keys():
            coef.update({i:poly[i]})
        else:
            coef.update({i:0})
    #print(coef)
    accu = 0
    for key in reversed(sorted(coef)):
        accu = (accu*x0)+coef[key]
    return accu

def pow_poly(poly, n):              # poly(x) ** n
    polypow = poly.copy()
    if(n==0):
        return 1
    for i in range(n-1):
        polypow = mul_poly(polypow,poly)
    return polypow

def combine_poly(poly1, poly2):     # poly1(poly2(x)), trudne!
    prod = []
    combined = {}
    if len(poly1) == 1 and 0 in poly1.keys():
        return poly1
    else:
        for key in poly1:
            if key != 0:
                prod.append(mul_poly(pow_poly(poly2,key),{0:poly1[key]}))
            if key == 0:
                prod.append({0:poly1[key]})
        for el in prod:
            combined = add_poly(combined,el)
        return combined

def diff_poly(poly):                # pochodna wielomianu
    der = {}
    for i in poly:
        if(i!=0):
            der.update({i-1:i*poly[i]})
    return der

p1 = {10: 1, 0: 2}            # W(x) = x**10 + 2
p2 = {100: 4, 5: 3}           # W(x) = 4 * x**100 + 3 * x**5
p3 = {0: 3}                   # W(x) = 3, wielomian zerowego stopnia
p4 = {0: 0}                   # zero
p5 = {5: 0}                   # zero (niejednoznaczność)

p6 = {10:2}
p7 = {10: 1, 0:2, 11: 2}

print(pow_poly(p1,2))
print(combine_poly(p2,{1:0}))
"""print(add_poly(p1,p6))
print(sub_poly(p1,p2))
print(mul_poly(p1,p2))
print(is_zero(p3))
print(cmp_poly(p1,p7))
print(eval_poly(p1,2))
print(pow_poly(p1,3))
print(diff_poly(p7))
print(mul_poly({10:1, 0:2},{0:3}))
print(combine_poly({2:5,0:3},{1:6,2:2}))
print(combine_poly({1:6,2:2},{2:5,0:3}))"""