with open("Never.txt", 'r') as file:
    # Read the lines of the file
    file_lines = file.readlines()
 
    # Print each line
    print("File Content:")
    for line in file_lines:
        print(line.strip())