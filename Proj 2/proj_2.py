# # # p_2 input
p_input = open("p2_input.txt", "r").readlines()

# # p_2 part 1
print((sum(int(dir[5:]) for dir in p_input if dir.find("down") != -1) - sum(int(dir[3:]) for dir in p_input if dir.find("up") != -1)) * sum(int(dir[8:]) for dir in p_input if dir.find("forward") != -1))

# # p_2 part 2
h_pos = 0
aim = 0
depth = 0
for dir in p_input:
    if dir.find("forward") == 0:
        h_pos += int(dir[8:])
        depth += int(dir[8:]) * aim
    elif dir.find("down") == 0:
        aim += int(dir[5:])
    elif dir.find("up") == 0:
        aim -= int(dir[3:])

print(depth * h_pos)