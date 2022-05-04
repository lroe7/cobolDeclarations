import random
import string
import csv


def randVarName():
    digits = random.randrange(1, 31)
    varName = ''
    countLetters = 0
    for i in range(0, digits):
        num = random.randrange(0, 10)
        if num == 0:
            newChar = str(random.randrange(0, 10))
        elif num == 1:
            newChar = '-'
        else:
            newChar = random.choice(string.ascii_letters)
            countLetters = 1
        varName = varName + newChar
    if varName[0] == '-':
        varName = randVarName()
    elif varName[digits - 1] == '-':
        varName = randVarName()
    elif countLetters == 0:
        varName = randVarName()
    return varName


dictionary = ["var", "Var", "num", "Num", "X", "x", "Z", "z", "user-input", "User-input","string", "String", "total",
              "Total", "add-num", "Add-Num", "add-Num", "ADD-num", "sub", "Sub", "sub-num", "sub-total", "Sub-total",
              "SUB-total", "interest", "Interest", "INTEREST", "dollar", "Dollar", "DOLLAR", "DOLLAR-USD", "Dollar-USD",
              "NumberOne", "numberOne", "Number-One", "NumberTwo", "numberTwo", "Number-Two", "quarterOne", "Quarter-One",
              "quarter-one", "QUARTER-ONE", "QuarterOne", "quarterTwo", "Quarter-Two","quarter-two", "QUARTER-TWO",
              "QuarterTwo", "quarterThree", "Quarter-Three", "quarter-three", "QUARTER-THREE", "QuarterThree",
              "quarterFour", "Quarter-Four", "quarter-four", "QUARTER-Four", "QuarterFour" ]

dataType = 'PIC'
dataSizes = ['9', 's9', 'x', 's9(13)v99', 's9(9)v99', '9v9(2)', '99', '9(2)', '9(2)v9(2)']
val = 'VALUE'
arr = []
for i in range (0, 100):
    ID = random.randrange(1, 100)
    if ID < 10:
        ID = '0' + str(ID)
    elif ID >= 50:
        ID = '01'

    # variable name randomization
    x = random.randrange(0, 101)
    if (x % 3) != 0:
        # pull from dictionary
        name = random.choice(dictionary)
    else:
        # random code with chars
        name = randVarName()
    num = random.randrange(0, 9)
    size = dataSizes[num]

    # 9 is the dataType, positive single digit int
    if num == 0:
        javaType = 'int'
        digits = random.randrange(1, 10)
        zero = random.randrange(0, 2)
        value = ''
        if zero == 0:
            size = size + '(' + str(0) + str(digits) + ')'
        else:
            size = size + '(' + str(digits) + ')'
        for i in range (0, digits):
            newchar = random.randrange(0, 10)
            value = value + str(newchar)
    # S9 is the data type, negative int
    elif num == 1:
        javaType = 'int'
        digits = random.randrange(1, 15)
        value = '-'
        size = size + '(' + str(digits) + ')'
        for i in range (0, digits):
            newchar = random.randrange(0, 10)
            value = value + str(newchar)
    # x( num ) is the data type
    elif num == 2:
        digits = random.randrange(1, 299)
        size = size + '(' + str(digits) + ')'
        countLetters = 0
        javaType = 'string'
        value = ''
        for i in range(0, digits):
            num = random.randrange(0, 10)
            if num == 0:
                newChar = str(random.randrange(0, 10))
            elif num == 1:
                newChar = '-'
            else:
                newChar = random.choice(string.ascii_letters)
                countLetters = 1
            value = value + str(newChar)
    # s9(13)v99 is the data type
    # value with sign, has 13 digits before the decimal and two after
    elif num == 3:
        javaType = 'double'
        value = ''
        for i in range(0, 12):
            newchar = random.randrange(0, 10)
            value = str(value) + str(newchar)
        value = value + str(round(random.random(), 2))

    # s9(9)v99 is the data type
    # value with sign, has 9 digits before the decimal and two after
    elif num == 4:
        javaType = 'double'
        value = ''
        for i in range(0, 8):
            newchar = random.randrange(0, 10)
            value = str(value) + str(newchar)
        value = value + str(round(random.random(), 2))

    # 9V9(2) is the dataType, one digit before the decimal and two after
    elif num == 5:
        javaType = 'double'
        value = round(random.uniform(0, 10), 2)

    # 99 is the data type, positive double digit int
    elif num == 6:
        javaType = 'int'
        value = random.randrange(10, 100)

    # 9(2) is the data type, positive double digit int (same as 99)
    elif num == 7:
        javaType = 'int'
        value = random.randrange(10, 100)

    # 9(2)V9(2) is the data type, double that has 2 digits before the decimal and 2 after
    elif num == 8:
        javaType = 'double'
        value = round(random.uniform(10, 100), 2)

    cobol = str(ID) + " " + str(name) + " " + str(dataType) + " " + str(size) + " " + str(val) + " " + str(value) + ' .'
    java = str(javaType) + " " + str(name) + " " + ' = ' + str(value) + ';'
    arr.append([cobol, java])


print(arr)
# header = ['cobol', 'java']
# data = arr
# with open('cobolToJava.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     writer.writerows(data)


