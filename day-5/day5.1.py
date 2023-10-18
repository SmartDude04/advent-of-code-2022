# Opening the file and storing it in a variable
file = open("day-5/day5-snippet.txt", "r")
# Making lines variable an array of the lines
lines = file.readlines()

# Remove \n from lines
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

# Make an array of the first part, the initial stack configuration
initial_stack = []
for line in lines:
    if(line == ""):
        break
    initial_stack.append(line)

# Make the stack arrays and then merge them into one big array
# Will finish with an array of the arrays of stacks, the top is at the end

# Know how many stacks there are and get rid of the last line that shows how many stacks there are
num_stacks = len(initial_stack[len(initial_stack) - 1].replace(" ", ""))
initial_stack.pop()

# Get rid of extra space between the letters that matter
for i in range(len(initial_stack)):
    # Ged rid of the first space
    initial_stack[i] = initial_stack[i][1:]
    
    initial_stack[i] = initial_stack[i].replace("[", "")
    initial_stack[i] = initial_stack[i].replace("]", "")
    initial_stack[i] = initial_stack[i].replace("   ", "-")
    initial_stack[i] = initial_stack[i].replace(" ", "")
    
    # for j in range((len(initial_stack[i]) - 1), -1, -1):
    #     if (j - 1) % 4 != 0:
    #         initial_stack[i].remove(j)
            
    print(initial_stack[i])
    
print(num_stacks)