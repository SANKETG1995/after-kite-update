def remove_lines_starting_with_integer(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.lstrip() and not line.lstrip()[0].isdigit():
                outfile.write(line)

if __name__ == "__main__":
    input_file = "file.txt"  # Replace with the path to your input file
    output_file = "file2.txt"  # Replace with the desired output file path
    remove_lines_starting_with_integer(input_file, output_file)
    print(f"Lines starting with integers removed and saved in '{output_file}'.")
    

    #print("No lines with integers found in the file.")

