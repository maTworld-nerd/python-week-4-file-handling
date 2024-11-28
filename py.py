# Defining a function to read from a file
def read_file(filename):
    try:
        with open(filename, 'r') as file:  # Opening in read mode
            content = file.read()  # Reading  and storing contents
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

# Defineing a function to modify the content
def modify_content(content):
    # Example modification: Convert text to uppercase and add a footer
    modified_content = content.upper() + "\n\n-- End of File --"
    return modified_content

# Defining a function to write to a new file
def write_to_file(new_filename, content):
    try:
        with open(new_filename, 'w') as file:  # Open in write mode
            file.write(content)  # Write modified content
        print(f"Modified content successfully written to '{new_filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Calling the functions in sequence
def main():
    input_filename = input("Enter the name of the file to read: ")
    original_content = read_file(input_filename)
    
    if original_content:  # Proceed if reading was successful
        modified_content = modify_content(original_content)
        output_filename = "modified_" + input_filename
        write_to_file(output_filename, modified_content)

# Printing a success message
main()


