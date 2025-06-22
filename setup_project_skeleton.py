import os
from pathlib import Path
import argparse

# Folder Structure
DIR_STRUCTURE = [
    ".github/workflows",
    "Artifacts",
    "final_model",
    "Network_Data",
    "data_schema",
    "logs",
    "prediction_output",
    "src/networksecurity/components",
    "src/networksecurity/constant",
    "src/networksecurity/entity",
    "src/networksecurity/logging",
    "src/networksecurity/exception",
    "src/networksecurity/pipeline",
    "src/networksecurity/utils",
    "src/networksecurity/cloud",
    "tests",
    "templates"
]

# File Structure
FILE_STRUCTURE = [
    ".gitignore",
    "README.md",
    "Dockerfile",
    "pyproject.toml",
    ".github/workflows/main.yml",
    "src/networksecurity/__init__.py"
]

def create_directories():
    for directory in DIR_STRUCTURE:
        Path(directory).mkdir(parents=True, exist_ok=True)

def create_files(force: bool):
    for file_path in FILE_STRUCTURE:
        path = Path(file_path)
        if path.exists() and not force:
            response = input(f"File '{file_path}' already exists. Overwrite? (y/N): ").strip().lower()
            if response != 'y':
                continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("")  # Create or clear the file

def main():
    parser = argparse.ArgumentParser(description="📦 Setup project skeleton.")
    parser.add_argument('-f', '--force', action='store_true', help='Force overwrite files without prompting.')
    args = parser.parse_args()

    create_directories()
    create_files(force=args.force)
    print("✅ Project skeleton created successfully.")

if __name__ == "__main__":
    main()
