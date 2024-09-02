def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is my first line.\n")
            file.write("This is the second line with a number: 42.\n")
            file.write("Finally, this is the third line.\n")
        print("File created and written successfully.")
        
    except (PermissionError, IOError) as e:
        print(f"Error writing to file: {e}")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("Contents of 'my_file.txt':")
            print(contents)
            
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied when trying to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Appending a new line: This is line four.\n")
            file.write("Appending another line: The number is 100.\n")
            file.write("Appending the last line: Goodbye!\n")
        print("Additional lines appended successfully.")
        
    except (PermissionError, IOError) as e:
        print(f"Error appending to file: {e}")

def main():
    create_file()        
    read_file()         
    append_to_file()    
    read_file()      

if __name__ == "__main__":
    main()
