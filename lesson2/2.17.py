line = "abcd cds bbs ghhhh sdjlkfj sdlkjf sdldkfj sssdfc zx xmnx xzxc nxc qwe ouqiweo qwoueoqiwuoe"
sortedline = sorted(line.split(), key=str.lower)
print(sortedline)

sortedline = sorted(line.split(), key=len)
print(sortedline)
