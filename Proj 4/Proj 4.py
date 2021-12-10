p_input = open("p4_input.txt", "r").read().splitlines()
p_input = [element for element in p_input if element != '']

all_boards = []

for i in range(len(p_input)):
    one_board = []
    for x in range(5):
        one_board.append(p_input[x])

    all_boards.append(one_board)

test = all_boards[0]

print(test[0, 2])
