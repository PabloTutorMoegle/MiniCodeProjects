# Archive Sorter
# This script sorts files in a specified directory into subdirectories based on their file extensions.
import os

#Dictionary of extensions 
# Define sets of extensions for each category
extensions = {
    'Text Files': {'txt', 'md', 'rtf', 'log', 'ini'},
    'Images': {'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg', 'webp', 'ico'},
    'PDFs': {'pdf'},
    'Word Documents': {'doc', 'docx', 'odt'},
    'Excel Sheets': {'xls', 'xlsx', 'ods', 'csv'},
    'Audio': {'mp3', 'wav', 'aac', 'flac', 'ogg', 'wma', 'm4a', 'opus'},
    'Video': {'mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv', 'webm', 'mpeg'},
    'Compressed': {'zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz'},
    'Executables': {'exe', 'msi', 'bat', 'sh', 'apk', 'jar', 'com', 'cmd'},
    'Presentations': {'ppt', 'pptx', 'odp'},
    'Code': {'py', 'js', 'java', 'c', 'h', 'cpp', 'hpp', 'cc', 'cs', 'html', 'css', 'php', 'rb', 'go', 'ts', 'swift', 'kt', 'rs', 'xml', 'json', 'yaml', 'yml'}
}


def sort_files_by_extension(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            ext = filename.split('.')[-1].lower()
            found = False
            for folder, exts in extensions.items():
                if ext in exts:
                    ext_dir = os.path.join(directory, folder)
                    found = True
                    break
            if not found:
                ext_dir = os.path.join(directory, 'Other Files')
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            os.rename(os.path.join(directory, filename), os.path.join(ext_dir, filename))

if __name__ == "__main__":
    directory = input("Enter the directory to sort files: ")
    if os.path.isdir(directory):
        sort_files_by_extension(directory)
        print(f"Files in '{directory}' have been sorted by extension.")
    else:
        print(f"The directory '{directory}' does not exist.")

