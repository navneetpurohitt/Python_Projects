import os
import shutil

def organize_files(folder_path):
    # Define folder names for different file types
    folders = {
        "Audio": [".mp3", ".wav", ".aac"],
        "Video": [".mp4", ".mkv", ".avi"],
        "PDFs": [".pdf"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".doc", ".docx", ".txt", ".xls", ".xlsx"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Scripts": [".py", ".js", ".html", ".css"]
    }

    # Create folders if they don't exist
    for folder_name in folders.keys():
        folder_dir = os.path.join(folder_path, folder_name)
        if not os.path.exists(folder_dir):
            os.makedirs(folder_dir)

    # Organize files into respective folders
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Move files to respective folders
        for folder_name, extensions in folders.items():
            if file_name.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(folder_path, folder_name, file_name))
                break

if __name__ == "__main__":
    folder_location = input("Enter the folder location to organize: ").strip()
    if os.path.exists(folder_location):
        organize_files(folder_location)
        print("Files have been organized successfully!")
    else:
        print("The provided folder location does not exist.")