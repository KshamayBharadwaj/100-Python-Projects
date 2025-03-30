import os
import shutil

# Define file categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Others": []  # Files that don't match any category
}

def organize_files(directory):
    """Organizes files in the specified directory."""
    if not os.path.exists(directory):
        print("Invalid directory!")
        return

    # Create folders
    for folder in CATEGORIES.keys():
        os.makedirs(os.path.join(directory, folder), exist_ok=True)

    # Move files
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):  # Ignore folders
            for category, extensions in CATEGORIES.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, category, file))
                    break
            else:
                shutil.move(file_path, os.path.join(directory, "Others", file))

    print("Files organized successfully!")

# Run the script
dir_path = input("Enter folder path: ")
organize_files(dir_path)
