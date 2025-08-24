import os

def process_file():
    """
    Function that prompts for a file, reads its content,
    converts it to uppercase, and saves it to a new file.
    Includes error handling for non-existent files.
    """
    while True:
        input_filename = input("Please, enter the input filename (e.g., my_text.txt): ")

        # Define the output filename. We add '_modified' to the original name.
        base_name, extension = os.path.splitext(input_filename)
        output_filename = f"{base_name}_modified{extension}"

        try:
            # Attempt to open and read the input file.
            # 'with open(...)' ensures the file is automatically closed.
            with open(input_filename, 'r', encoding='utf-8') as input_file:
                content = input_file.read()
            
            # Modify the content: convert to uppercase
            modified_content = content.upper()
            
            # Write the modified content to the new file
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(modified_content)
                
            print(f"✅ File read successfully: '{input_filename}'")
            print(f"✍️ Modified content saved to: '{output_filename}'")
            print("🎉 Operation completed successfully!")
            break  # Exit the loop, as the operation was successful

        except FileNotFoundError:
            # Handle the error if the file is not found
            print(f"❌ Error: The file '{input_filename}' was not found.")
            print("Please check the filename and try again.\n")

# Call the main function to run the program
if __name__ == "__main__":
    process_file()