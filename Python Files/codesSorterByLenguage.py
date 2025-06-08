import os

#Dictionary of extensions 
# Define sets of extensions for each category
extensions = {
    'C++ Files': {'cpp', 'h', 'hpp', 'cc'},
    'C# Files': {'cs'},
    'C Files': {'c'},
    'Json Files': {'json'},
    'XML Files': {'xml'},
    'Python Files': {'py'},
    'Java Files': {'java'},
    'JavaScript Files': {'js', 'ts'},
    'HTML Files': {'html', 'htm'},
    'CSS Files': {'css'},
    'PHP Files': {'php'},
    'Ruby Files': {'rb'},
    'Go Files': {'go'},
    'Swift Files': {'swift'}
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
    directory = os.path.dirname(os.path.abspath(__file__))
    sort_files_by_extension(directory)
    print(f"Files in '{directory}' have been sorted by extension.")
