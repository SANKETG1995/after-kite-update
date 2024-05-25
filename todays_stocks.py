import re

def clean_and_strip(line):
    # Use regular expression to remove special characters and numbers
    cleaned_line = re.sub(r'[^A-Za-z\s]', '', line)
    return cleaned_line.strip()

def remove_special_and_numbers(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            cleaned_line = clean_and_strip(line)
            outfile.write(cleaned_line + '\n')

# Replace 'input_file.txt' with the actual path to your input file
# Replace 'output_file.txt' with the desired path for the cleaned output


def clean_and_get_non_duplicates(input_file):
    # Read content from the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove special characters and numbers, keep only alphabetic characters and spaces
    cleaned_content = re.sub(r'[^a-zA-Z\s]', '', content)

    # Split the cleaned content into words
    words = cleaned_content.split()

    # Get non-duplicate words as a list
    non_duplicates = list(set(words))

    return non_duplicates

# Specify the input file
input_file = 'output_file.txt'  # Replace with the actual path to your file

# Call the function
result = clean_and_get_non_duplicates(input_file)

# Print each non-duplicate word on a new line
for word in result:
    print(word)




