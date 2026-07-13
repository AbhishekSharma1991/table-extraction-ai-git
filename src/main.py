import os

print("Table Extraction Project Started")

input_folder = "input"

if not os.path.exists(input_folder):
    print(f"Folder '{input_folder}' does not exist!")
else:
    files = os.listdir(input_folder)
    print("Files found:", files)