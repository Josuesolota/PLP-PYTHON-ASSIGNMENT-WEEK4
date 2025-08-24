### **File Processor**

This is a simple Python program that demonstrates how to read from a file, modify its content, and write the modified content to a new file. It also includes robust error handling to manage cases where the input file does not exist.

-----

### **Features**

  * **File Reading**: Reads text content from a user-specified file.
  * **Content Modification**: Converts all text to uppercase.
  * **File Writing**: Creates a new file to save the modified content.
  * **Error Handling**: Gracefully handles `FileNotFoundError` if the specified input file is not found, prompting the user to try again.

-----

### **How to Use**

#### **Prerequisites**

You only need Python 3 installed on your system.

#### **Setup**

1.  **Save the Code**: Save the provided Python code in a file named `process_files.py`.
2.  **Create a Test File**: In the same directory, create a text file for the program to read. Name it `my_text.txt` and add some content to it.

#### **Execution**

1.  Open your terminal or command prompt.

2.  Navigate to the directory where you saved your files.

3.  Run the program using the following command:

    ```bash
    python process_files.py
    ```

4.  When prompted, enter the name of your test file (e.g., `my_text.txt`).

#### **Expected Output**

  * The program will read the content of `my_text.txt`.
  * It will create a new file named `my_text_modified.txt`.
  * The content of the new file will be the uppercase version of the original text.

-----

### **Error Handling Example**

If you run the program and enter a filename that does not exist (e.g., `nonexistent.txt`), the program will display an error message and allow you to try again without crashing.

```
❌ Error: The file 'nonexistent.txt' was not found.
Please check the filename and try again.
```
