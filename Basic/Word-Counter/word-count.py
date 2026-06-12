# Word Counter Program

try:
    # User enters file name
    filename = "C:\\Users\\bisha\\OneDrive\\Desktop\\Python-Project-Collection\\Basic\\Word-Counter\\simple.txt"

    # Open file
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    # Count words
    words = content.split()
    word_count = len(words)

    print("\nTotal number of words:", word_count)

except FileNotFoundError:
    print("\nError: File not found.")
    print("Make sure the text file is in the same folder as your Python file.")

except Exception as e:
    print("\nAn error occurred:", e)
