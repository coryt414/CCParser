import file_len
totalLines = file_len.file_len('Transactions-Download-01-26-2017.csv')
with open('Transactions-Download-01-26-2017.csv') as f:
    # Read headings and assign to variables
    lineOne = f.readline()
    lineOne = lineOne.split(', ')
    transactionDate = lineOne[1]
    purchaseDescription = lineOne[4]
    rawCategory = lineOne[5]
    print(lineOne)
    # Read file
    # string = f.read()
    totalExpenses = []
    for i in range(1, totalLines + 1):
        purchaseInfo = f.readline()
        purchaseInfo = purchaseInfo.split(',')
        if purchaseInfo[6] != '':
            print('Purchase #' + str(i) + ': $' + purchaseInfo[6])
            currentAmount = float(purchaseInfo[6])
            round(currentAmount, 2)
            # print(currentAmount)
            totalExpenses.append(currentAmount)
            # print(totalExpenses)
        else:
            print('Purchase #' + str(i) + ': $' + purchaseInfo[7].rstrip('\n'))
            currentAmount = float(purchaseInfo[7])
            round(currentAmount, 2)
            # print(currentAmount)
            totalExpenses.append(currentAmount)
        if i == 78:
            print((round(sum(totalExpenses), 2)))
