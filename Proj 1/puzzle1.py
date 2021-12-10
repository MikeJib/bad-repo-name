with open ('puzzle1_input.txt') as file:
    # Part 1
    input = [int(x) for x in file.read().splitlines()]
    print(sum(1 for i in range(len(input)-1) if input[i+1] > input[i]))

    # Part 2
    input_windows = [sum(input[i:i+3]) for i in range(len(input) - 2)]
    print(sum(1 for i in range(len(input_windows) - 1) if input_windows[i+1] > input_windows[i]))
