# Read and Write Challenge
try:
    # Create and write to a new file
    with open("input.txt", "w") as file:

        # Write some content to the file
        file.write("This is the initial content of the file.")

    print("File 'input.txt' has been created with initial content.")

    # Open the original file in read mode
    with open("input.txt", "r") as input_file:
        # Read content from the file
        content = input_file.read()

    # Modify the content (make it uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open("output.txt", "w") as output_file:
        output_file.write(modified_content)

    print("Content has been successfully modified and saved to 'output.txt'")
except FileNotFoundError:
    print("Error: The 'input.txt' file does not exist.")
except IOError:
    print("Error: Unable to read/write files.")
