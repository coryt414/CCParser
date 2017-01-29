purchaseInfo = [0, 1, 2, 3, 4, 5, '$128.15\n']
noNewLine = purchaseInfo[6]
print(type(noNewLine))
noNewLine2 = noNewLine[(0, (int(len(noNewLine) - 2)))]