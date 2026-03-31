import os
import shutil
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    filename='file_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define file categories
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.wmv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Others': []
}

def create_subfolders(target_directory):
    """Create subfolders for file categories if they don't exist."""
    for category in FILE_CATEGORIES.keys():
        folder_path = target_directory / category
        if not folder_path.exists():
            folder_path.mkdir()
            logging.info(f"Created folder: {folder_path}")

def categorize_file(file_name):
    """Categorize file based on its extension."""
    file_extension = Path(file_name).suffix.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    return 'Others'

def handle_duplicates(destination_path):
    """Handle duplicate filenames by appending a number."""
    if destination_path.exists():
        base = destination_path.stem
        extension = destination_path.suffix
        counter = 1
        while destination_path.exists():
            destination_path = destination_path.parent / f"{base}({counter}){extension}"
            counter += 1
    return destination_path

def organize_files(target_directory):
    """Organize files in the target directory."""
    for item in target_directory.iterdir():
        if item.is_file():
            category = categorize_file(item.name)
            destination_folder = target_directory / category
            destination_path = destination_folder / item.name

            # Handle duplicate filenames
            destination_path = handle_duplicates(destination_path)

            try:
                shutil.move(str(item), str(destination_path))
                logging.info(f"Moved file: {item.name} -> {destination_path}")
            except Exception as e:
                logging.error(f"Error moving file {item.name}: {e}")
        elif item.is_dir() and item.name not in FILE_CATEGORIES.keys():
            logging.info(f"Skipped folder: {item.name}")

def main():
    # Define the target directory (e.g., Downloads folder)
    target_directory = Path.home() / 'Downloads'

    # Ensure the target directory exists
    if not target_directory.exists():
        logging.error(f"Target directory does not exist: {target_directory}")
        return

    # Create subfolders for file categories
    create_subfolders(target_directory)

    # Organize files in the target directory
    organize_files(target_directory)

if __name__ == "__main__":
    main()