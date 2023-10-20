# Opening the file and storing it in a variable
# file = open("day-5/day5.txt", "r")
file = open("day-5/day5.txt", "r")
# Making lines variable an array of the lines
lines = file.readlines()

# Remove \n from lines
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

# Make an array of the first part, the initial stack configuration
crates = []
for line in lines:
    if(line == ""):
        break
    crates.append(line)

# Make the stack arrays and then merge them into one big array
# Will finish with an array of the arrays of stacks, the top is at the end

# Know how many stacks there are and get rid of the last line that shows how many stacks there are
num_stacks = len(crates[len(crates) - 1].replace(" ", ""))
crates.pop()

# Get rid of extra space between the letters that do not matter
for i in range(len(crates)):
    # Ged rid of the first space
    crates[i] = crates[i][1:]
    
    crates[i] = crates[i].replace("[", "")
    crates[i] = crates[i].replace("]", "")
    crates[i] = crates[i].replace("    ", "   ")
    crates[i] = crates[i].replace("   ", "-")
    crates[i] = crates[i].replace(" ", "")
    
    # for j in range((len(crates[i]) - 1), -1, -1):
    #     if (j - 1) % 4 != 0:
    #         crates[i].remove(j)
            
    # print(crates[i])

old_crates = crates
crates = []
# Make the arrays of the stacks. Index 0 is at the bottom of the stack array 0 in the full array is stack 1
for i in range(num_stacks):
    single_stack = []
    # Start at the bottom of the first stack, which is the first element in the last item in the list
    for j in range(len(old_crates) - 1, -1, -1):
        if(old_crates[j][i] != "-"):
            single_stack.append(old_crates[j][i])
    
    crates.append(single_stack)
    

print(crates)


# Get the list of the moving commands
start_point = len(old_crates) + 2
move_list = lines[start_point:]
move_commands =[]

# Parse the move list and get just the numbers needed and put them in an array of arrays
# Turn into an array of the three numbers we need, [[amount], [from], [to]]
for i in range(len(move_list)):
    move_list[i] = move_list[i].translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'})
    move_list[i] = move_list[i][1:]
    temp_move = move_list[i].split("  ")
    temp_move = [int(i) for i in temp_move]
    move_commands.append(temp_move)


# Move all items
for move in move_commands:
    # Figure out where we are coming from what where we are going to
    from_row = move[1]
    to_row = move[2]
    
    move_crates = []
    
    # Loop for as many items as we need
    for i in range(move[0]):
        item = crates[from_row - 1].pop()
        # crates[to_row - 1].append(item)
        move_crates.append(item)
    
    move_crates.reverse()
    
    for crate in move_crates:
        crates[to_row - 1].append(crate)
        

top_boxes = ""
for row in crates:
    top_boxes = top_boxes + row.pop()
    
print(top_boxes)