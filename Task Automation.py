import os
import shutil

def organize_images():
    # Get the current directory where the script is running
    current_folder = os.getcwd()
    
    # Name of the new folder to create
    new_folder_name = "Organized_Images"
    new_folder_path = os.path.join(current_folder, new_folder_name)

    # 1. Create the new folder if it doesn't exist
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print(f"Created folder: {new_folder_name}")

    # 2. Loop through files in the current directory
    files_moved = 0
    for filename in os.listdir(current_folder):
        # Check if file is a .jpg
        if filename.endswith(".jpg"):
            source = os.path.join(current_folder, filename)
            destination = os.path.join(new_folder_path, filename)
            
            # Move the file
            shutil.move(source, destination)
            print(f"Moved: {filename}")
            files_moved += 1

    print(f"\nTask Complete! Moved {files_moved} images to '{new_folder_name}'.")

if __name__ == "__main__":
    organize_images()