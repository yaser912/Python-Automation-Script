from pathlib import Path
import shutil

# Dictionary mapping file extensions to destination folders
file_types = {
    ".zip": "Archives",
    ".exe": "Executables",
    ".pdf": "PDF",
    ".docx": "Microsoft Word Docs",
    ".py": "Python Files",
    ".ipynb": "Python Files",
    ".msi": "Windows Installer",
    ".gz": "TAR Archives",
    ".mp4": "MP4 Files"
}

cwd = Path("C:\\Users\\yaser\\Downloads")

for file in cwd.iterdir():
    file_type = file_types.get(file.suffix)
    if file_type:
        destination = cwd / file_type
        destination.mkdir(parents=True, exist_ok=True)
        shutil.move(str(file), str(destination))