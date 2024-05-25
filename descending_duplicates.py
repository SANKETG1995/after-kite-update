def find_and_display_lines_in_descending_order(input_file):
    lines_with_integers = []  # List to store (line, integers) tuples
    with open(input_file, 'r') as infile:
        for line in infile:
            # Use regular expressions to find all integers in the line
            line_integers = [int(s) for s in line.split() if s.isdigit()]
            if line_integers:
                lines_with_integers.append((line, line_integers))

    # Sort the list of (line, integers) tuples based on the integers in descending order
    lines_with_integers.sort(key=lambda x: x[1], reverse=True)

    if lines_with_integers:
        print("Lines with integers in descending order:")
        for line, _ in lines_with_integers:
            print(line, end="")
    else:
        print("No lines with integers found in the file.")

if __name__ == "__main__":
    input_file = "file2.txt"  # Replace with the path to your input file
    find_and_display_lines_in_descending_order(input_file)

