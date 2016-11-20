
#1
romanNumbers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

#2
keys = ["I","V","X","L","C","D","M"]
values = [1,5,10,50,100,500,1000]
romanNumbers = dict(zip(keys,values))

#3
for (k,v) in zip(keys,values):
    romanNumbers[k] = v

#4
romanNumbers['I'] = 1
romanNumbers['V'] = 5
romanNumbers['X'] = 10
romanNumbers['L'] = 50
romanNumbers['C'] = 100
romanNumbers['D'] = 500
romanNumbers['M'] = 1000

#5
romanNumbers.update({'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000})


def roman2int(roman):
    number = 0
    prev = 0
    for num in reversed(roman):
        tmp = romanNumbers[num]
        if tmp < prev:
            number -= tmp
        else:
            number += tmp
        prev = tmp
    return number

print(roman2int("MCMLIV"))
