import os
import shutil

# Define the current file name and the new file name
current_file_name = "old_file.txt"
new_file_name = "new_file.txt"

# Rename the file
os.rename(current_file_name, new_file_name)

print(f"File '{current_file_name}' has been renamed to '{new_file_name}'.")

# Define the current file name and the new file name
current_file_name = "old_file.txt"
new_file_name = "new_file.txt"

# Rename the file
shutil.move(current_file_name, new_file_name)

print(f"File '{current_file_name}' has been renamed to '{newfile_name}'.")