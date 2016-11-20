line = "abx \t cdy \t efz \t ghw \t iju \t klv \t"
result = sum(len(x) for x in line.split())
print(result)
