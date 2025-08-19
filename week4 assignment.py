#create a program that reads a file and writes a modified version to a new file
#1 program that reads
with open("databases.txt","r") as file:
    content=file.read()

file2=content.upper()
#2 program that writes
with open("modified_databases.txt","w") as new_file:
    new_file.write(file2)


#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
    print("\n✅ File read successfully!")
    print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
