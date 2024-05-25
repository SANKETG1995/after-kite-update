def find_long_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            long_words = [word for word in words if len(word) > 15]
            return long_words
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = 'find15.txt'
result = find_long_words_in_file(file_path)
if result is not None:
    print(f"Words with more than 15 characters in '{file_path}':")
    for word in result:
        print(word)