import os
import shutil

def create_destination_directories(dest_dir):
    # Create destination directories if they don't exist
    directories = ['Images', 'Videos', 'Audios', 'Documents', 'Software', 'Other']
    for directory in directories:
        os.makedirs(os.path.join(dest_dir, directory), exist_ok=True)

def get_file_type(filename):
    # Determine the type of the file based on its extension
    file_extensions = {
        'Images': ('.png', '.jpg', '.jpeg', '.gif'),
        'Videos': ('.mp4', '.avi', '.mkv'),
        'Audios': ('.mp3', '.wav', '.flac'),
        'Documents': ('.pdf', '.doc', '.docx', '.txt'),
        'Software': ('.exe', '.msi')
    }
    for file_type, extensions in file_extensions.items():
        if filename.lower().endswith(extensions):
            return file_type
    return 'Other'

def move_files(source_dir, dest_dir):
    create_destination_directories(dest_dir)
    
    # Iterate over files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        file_type = get_file_type(filename)

        # Move file to appropriate folder
        dest_folder = os.path.join(dest_dir, file_type)
        shutil.move(source_file, dest_folder)

def main():
    # source_dir = "SourceDir/"
    # dest_dir = "DestinationDir/"

    source_dir = input("Enter source directory path: ").strip()
    dest_dir = input("Enter destination directory path: ").strip()

    if not os.path.exists(source_dir):
        print("Source directory does not exist.")
        return
    if not os.path.exists(dest_dir):
        print("Destination directory does not exist.")
        return

    move_files(source_dir, dest_dir)
    print("Files were moved successfully.")

import os

def create_fake_files(directory):
    # Define file extensions for each category
    file_extensions = {
        'Images': ('.png', '.jpg', '.jpeg', '.gif'),
        'Videos': ('.mp4', '.avi', '.mkv'),
        'Audios': ('.mp3', '.wav', '.flac'),
        'Documents': ('.pdf', '.doc', '.docx', '.txt'),
        'Software': ('.exe', '.msi')
    }
    
    for category, extensions in file_extensions.items():
        category_directory = os.path.join(directory, category)
        os.makedirs(category_directory, exist_ok=True)  
        
        for extension in extensions:
            filename = f"fake_{category.lower()}{extensions.index(extension) + 1}"
            file_path = os.path.join(category_directory, filename + extension)
            file_path = os.path.join(filename + extension)
            with open(file_path, 'w') as file:
                file.write(f"This is a fake {category.lower()} file with {extension} extension.")

            print(f"Fake file '{filename}{extension}' created successfully in '{category_directory}'.")


if __name__ == "__main__":
    # create_fake_files('SourceDir')
    main()
