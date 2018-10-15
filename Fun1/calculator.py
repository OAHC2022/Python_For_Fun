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
    my thought on converting to polish notation: count from the last calculation symbol to the first.
    if I find a "+" or "-", then I extend the previous numbers to the "Reverse_Polish_n" list and then extend the previous calculation symbols.
    Finally, I extend all the rest to the list.
    Each block is like: a+b+c*d+ {there is always a addition/subtraction after the mul/div}
    """
    calc = calc[::-1]
    num = num[::-1]
    revere_polish_n = []
    num_j = 0
    calc_j = 0
    for i in range(len(calc)):
        if calc[i] in "+":
            revere_polish_n.extend(num[num_j:i + 1])
            if i > calc_j:
                revere_polish_n.extend(calc[calc_j:i][::-1])
            num_j = i + 1
            calc_j = i
            print(revere_polish_n)

    revere_polish_n.extend(num[num_j:])
    revere_polish_n.extend(calc[calc_j:][::-1])
    print(revere_polish_n, num, calc,calc_j)

    # convert the first value to negative if it is negative
    if first_value_negative:
        for counter, val in enumerate(revere_polish_n[::-1]):
            if val not in "+-*/":
                revere_polish_n[len(revere_polish_n) - 1 - counter] = str(-int(revere_polish_n[::-1][counter]))
                break

    # calculate!
    stack_num = []
    for i in range(len(revere_polish_n)):
        if revere_polish_n[i] not in "+-*/":
            stack_num.append(int(revere_polish_n[i]))
        else:
            if revere_polish_n[i] == "+":
                stack_num[-2] = stack_num[-1] + stack_num[-2]
                stack_num.remove(stack_num[-1])
            if revere_polish_n[i] == "-":
                stack_num[-2] = stack_num[-1] - stack_num[-2]
                stack_num.remove(stack_num[-1])
            if revere_polish_n[i] == "*":
                stack_num[-2] = stack_num[-1] * stack_num[-2]
                stack_num.remove(stack_num[-1])
            if revere_polish_n[i] == "/":
                stack_num[-2] = stack_num[-1] / stack_num[-2]
                stack_num.remove(stack_num[-1])

    return stack_num[0]


if __name__ == "__main__":
    string = sys.stdin.readline().strip()
    print(binop(string))
