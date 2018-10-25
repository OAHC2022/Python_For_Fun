"""Use Polish Reverse Notation to make a simple calculator!!"""
import sys

def binop(string):
    # record the value
    string = string.replace(" ", "").strip()
    num = []
    calc = []
    j = 0
    first_value_negative = False
    if string[0] == "-":
        first_value_negative = True
        string = string[1:]
    for i, val in enumerate(string):
        if val in "+-*/":
            calc.append(val)
            num.append(string[j:i])
            j = i + 1
    num.append(string[j:])
    # Create Reverse Polish Notation
    """
    Revision: my thought on converting to polish notation: count from the last calculation symbol to the first.
    Always group number with */ togther and calculate their value. Then stack all +- signs in the end
    """
    calc = calc[::-1]
    num = num[::-1]
    revere_polish_n = num.copy()
    calc_temp = []
    symbol_num = 0
    """Find all the */"""
    for i in range(len(calc)):
        if calc[i] in "*/" and i == len(calc) - 1:
            calc_temp.append(calc[i])
            for k in range(len(calc_temp)):
                revere_polish_n.insert(k + i + 2 + symbol_num, calc_temp[-k])
        elif calc[i] in "*/":
            calc_temp.append(calc[i])
        else:
            for k in range(len(calc_temp)):
                revere_polish_n.insert(k + i + 1 + symbol_num, calc_temp[::-1][k])
            symbol_num += len(calc_temp)
            calc_temp = []
    calc_temp = []
    """append the rest of the +- into the stack"""
    for i in calc:
        if i in "+-":
            calc_temp.append(i)
    revere_polish_n.extend(calc_temp[::-1])

    # convert the first value to negative if it is negative
    if first_value_negative:
        for counter, val in enumerate(revere_polish_n[::-1]):
            if val not in "+-*/":
                revere_polish_n[len(revere_polish_n) - 1 - counter] = str(-int(revere_polish_n[::-1][counter]))
                break

    # calculate with stack!
    stack_num = []
    for i in range(len(revere_polish_n)):
        if revere_polish_n[i] not in "+-*/":
            stack_num.append(int(revere_polish_n[i]))
        else:
            if revere_polish_n[i] == "+":
                stack_num[-2] = stack_num[-1] + stack_num[-2]
                del stack_num[-1]
            if revere_polish_n[i] == "-":
                stack_num[-2] = stack_num[-1] - stack_num[-2]
                del stack_num[-1]
            if revere_polish_n[i] == "*":
                stack_num[-2] = stack_num[-1] * stack_num[-2]
                del stack_num[-1]
            if revere_polish_n[i] == "/":
                stack_num[-2] = stack_num[-1] / stack_num[-2]
                del stack_num[-1]
    print(stack_num[0])


if __name__ == "__main__":
    string = sys.stdin.readline().strip()
    binop(string)
