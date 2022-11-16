import re


def arithmetic_arranger(arg1, arg2=True):
    line1 = line2 = line3 = line4 = ''
    # Error 1
    if len(arg1) > 5:
        print("Error: Too many problems.")
        return

    for y in arg1:
        x = y.split()
        # Error 2
        if not (x[1] == '+' or x[1] == '-'):
            print("Error: Operator must be '+' or '-'.")
            return

        # Error 3
        re1 = re.search('\D', x[0])
        re2 = re.search('\D', x[2])
        if re1 or re2:
            print('Error: Numbers must only contain digits.')
            return

        # Error 4
        if len(x[0]) > 4 or len(x[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return

    for y in arg1:
        x = y.split()
        space1 = len(x[0]) - len(x[2])  # integer
        addition = str(int(x[0]) + int(x[2]))  # string
        subtraction = int(x[0]) - int(x[2])  # integer
        max_value = str(max(int(x[0]), int(x[2])))  # string
        if space1 > 0:
            line1 += ' '*2 + x[0] + ' '*4
            line2 += x[1] + ' '*(abs(space1) + 1) + x[2] + ' '*4
            line3 += '-'*(len(x[0]) + 2) + ' '*4
        else:
            line1 += ' '*(abs(space1) + 2) + x[0] + ' '*4
            line2 += x[1] + ' ' + x[2] + ' '*4
            line3 += '-'*(len(x[2]) + 2) + ' '*4

        if x[1] == "+":
            if len(addition) == len(max_value):
                line4 += ' '*2 + addition + " "*4
            else:
                line4 += ' ' + addition + " "*4
        elif x[1] == '-':
            if len(str(abs(subtraction))) == len(max_value):
                if subtraction < 0:
                    line4 += ' ' + str(subtraction) + " "*4
                else:
                    line4 += ' '*2 + str(subtraction) + " "*4
            else:
                if subtraction < 0:
                    line4 += ' ' * \
                        (len(max_value) - len(str(abs(subtraction))) + 1) + \
                        str(subtraction) + " "*4
                else:
                    line4 += ' ' * \
                        (len(max_value) - len(str(subtraction)) + 2) + \
                        str(subtraction) + " "*4

    # print(len(line1), len(line2), len(line3), len(line4))
    if arg2:
        print('{0}\n{1}\n{2}\n{3}'.format(
            line1[:-4], line2[:-4], line3[:-4], line4[:-4]))
    else:
        print('{0}\n{1}\n{2}'.format(line1[:-4], line2[:-4], line3[:-4]))
    return


# arithmetic_arranger(["3 + 8", "75 + 38", "999 + 999", "5230 + 4900"], True)
# arithmetic_arranger(["32 + 40", "10 + 38", "425 + 175", "5250 + 1349"], False)
# arithmetic_arranger(["50 - 30", "1000 - 801", "9990 - 999", "523 - 49"], True)
# arithmetic_arranger(["5 - 30", "1 - 3801", "9 - 9999", "23 - 490"], True)
