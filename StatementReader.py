import file_len
totalLines = file_len.file_len('Transactions-Download-02-15-2017.csv')
with open('Transactions-Download-02-15-2017.csv') as f:
    # Read headings and assign to variables
    # lineOne = f.readline()
    # lineOne = lineOne.split(', ')
    # Read file
    # string = f.read()
    totalSum = []
    f.readline()[2:]
    for line in range(2, totalLines +1):
        line = f.readline()
        stage, transactionDate, postedDate, cardNumber, purchaseDescription, purchaseCategory, purchaseDebit, purchaseCredit = line.split(',')
        if purchaseCategory != 'Payment' and purchaseDescription != 'CREDIT-CASH BACK REWARD':
            print(purchaseDescription)
            print(purchaseCategory)
            if purchaseDebit != '':
                totalSum.append(float(purchaseDebit))
            else:
                purchaseCredit = purchaseCredit.split()
                totalSum.append(float(purchaseCredit[0]))
    sum = 0
    for value in totalSum:
        sum += value
        # print sum with 2 decimal places
    print('% .2f' % sum)

