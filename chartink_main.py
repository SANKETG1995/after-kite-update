import subprocess


# Run the other script
process=subprocess.run(["python", "chartink.py"], capture_output=True)

output=process.stdout.decode("utf-8")

# Write the output to a file
output_file_path = "file.txt"
with open(output_file_path, "w") as file:
    file.write(output)

# Run the other script
process=subprocess.run(["python", "sorter.py"], capture_output=True)

output=process.stdout.decode("utf-8")

# Write the output to a file
output_file_path = "file.txt"
with open(output_file_path, "w") as file:
    file.write(output)

subprocess.run(["python", "removeint.py"])

subprocess.run(["python", "descending_duplicates.py"])
