line = "word \t abcdsd \t lkjldfkj \t slf \t sdfdsfs \t"
sortedwords = sorted(line.split(), key=len)
shortest = sortedwords[0]
longest = sortedwords[-1]
print(longest, len(longest))

#print(shortest, len(shortest))
#print(shortest,longest)
