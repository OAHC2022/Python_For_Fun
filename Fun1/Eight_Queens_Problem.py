import random

queen_pos = [1, 2, 3, 4, 5, 6, 7, 8]
#Queen can be any length element

# i is from 1 - 8
def check(lst, i):
    """
    Check if position is good
    :param lst: the eight queen list
    :param i: index of the eight queen list
    :return: Check if each element in the list meets the constraint
    """
    for k in range(i - 1):
        if lst[k] == lst[i]:
            return False
        if lst[k] - lst[i] == k - i:
            return False
        if lst[k] - lst[i] == i - k:
            return False
    return True


def draw_board(lst):
    """
    Draw the board
    :param lst: the eight queen list
    :return: the string representation of the board
    """
    board = ""
    board += "_{:_^1}".format("_") * len(lst) + "\n"
    for row in range(len(lst)):
        for column in range(len(lst)):
            if lst[column] == len(lst) - row:
                board += "|{:_^1.5}".format("O")
            else:
                board += "|{:_^1.5}".format("_")
        board += "|\n"
    print(board)


if __name__ == "__main__":
    found_it = False
    print("initial board")
    draw_board(queen_pos)
    count = 1
    while True:
        random.shuffle(queen_pos)
        print("{} times to try".format(count))
        draw_board(queen_pos)
        for i in range(1, len(queen_pos)):
            if not check(queen_pos, i):
                break
            if i == len(queen_pos) - 1:
                print("Found it!! it is {}".format(queen_pos))
                found_it = True
        if found_it == True:
            break
        count += 1
    draw_board(queen_pos)
