from pathlib import Path

# Get the current working directory
current_directory = Path.cwd()

print(f"Contents of '{current_directory}':\n")

# Iterate through all items in the directory
for item in current_directory.iterdir():
    # Check if it's a file or a folder to make the output cleaner
    item_type = "📁 Folder" if item.is_dir() else "📄 File"
    print(f"{item_type}: {item.name}")