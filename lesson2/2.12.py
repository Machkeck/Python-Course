line = "abx \t cdy \t efz \t ghw \t iju \t klv \t"
L = line.split()
result1 = ""
for element in L:
    result1+=(element[0])
print(result1)

result2 = ""
for element in L:
    result2+=element[len(element)-1]
print(result2)
