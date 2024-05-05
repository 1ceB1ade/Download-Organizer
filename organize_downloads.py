import os
import shutil
import getpass

def organize_downloads(download_dir):
    file_types = {
        "Documents": [".pdf", ".doc", ".docx", ".txt"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Music": [".mp3", ".wav", ".flac"],
        "Archives": [".zip", ".rar", ".7z"],
        "Executables": [".exe", ".msi"],
        "Scripts": [".py", ".sh", ".bat"]
    }

    for folder in file_types.keys():
        folder_path = os.path.join(download_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for filename in os.listdir(download_dir):
        if os.path.isfile(os.path.join(download_dir, filename)):
            src_file = os.path.join(download_dir, filename)
            file_ext = os.path.splitext(filename)[1].lower()

            dest_folder = "Other"  # Default folder
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    dest_folder = folder
                    break

            dest_path = os.path.join(download_dir, dest_folder)
            shutil.move(src_file, dest_path)
            print(f"Moved {filename} to {dest_folder} folder.")

if __name__ == "__main__":
    username = getpass.getuser()
    download_dir = os.path.join("C:\\Users", username, "Downloads")
    organize_downloads(download_dir)
    
    input("Press Enter to exit...")
