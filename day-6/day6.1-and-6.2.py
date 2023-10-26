import time
start = time.perf_counter()
def check_if_match(num_chars):
    # Opening the file and storing it in a variable
    file = open("day-6/day6.txt", "r")

    string = [*file.readline()]
    
    for i in range(len(string) - (num_chars - 1)):
        test_string = string[i:i+num_chars]
        if(len(test_string) == len(set(test_string))):
            print(i + num_chars)
            break

check_if_match(4)
check_if_match(14)

end = time.perf_counter()
print(f"Completed in: {str((end - start) * 1000)} ms")

# Things learned:
    # enumerate() method
    # zip() method
    # F-strings