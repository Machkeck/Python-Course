L = [12, 1, 2, 13, 12, 99, 999, 67, 234, 11, 23, 90, 10, 887]
line = " ".join(str(x).zfill(3) for x in L)
print(line)