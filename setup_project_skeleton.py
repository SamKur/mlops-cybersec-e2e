from pathlib import Path
import argparse

# Base folder structure for a clean MLOps-ready Python project
DIR_STRUCTURE = [
    ".github/workflows",
    "src/project_name/components",
    "src/project_name/config",
    "src/project_name/core",
    "src/project_name/entity",
    "src/project_name/utils",
    "src/project_name/pipeline",
    "src/project_name/cloud",
    "src/project_name",
    "tests",
    "configs",
    "notebooks",
    "scripts",
    "artifacts",
    "logs",
    "data"
]

FILE_STRUCTURE = [
    ".gitignore",
    "README.md",
    "Dockerfile",
    "pyproject.toml",
    "requirements.txt",
    ".github/workflows/main.yml",
    "src/project_name/__init__.py"
]

def create_directories():
    for directory in DIR_STRUCTURE:
        Path(directory).mkdir(parents=True, exist_ok=True)

def create_files(force: bool):
    for file_path in FILE_STRUCTURE:
        path = Path(file_path)
        if path.exists() and not force:
            response = input(f"File '{file_path}' exists. Overwrite? (y/N): ").strip().lower()
            if response != 'y':
                continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("")

def create_init_files(base_package: str):
    base_path = Path(base_package)
    if base_path.exists():
        for subdir in base_path.rglob("*"):
            if subdir.is_dir():
                init_file = subdir / "__init__.py"
                init_file.touch(exist_ok=True)

def main():
    parser = argparse.ArgumentParser(description="🛠️ Setup a clean, reusable MLOps project structure.")
    parser.add_argument('-f', '--force', action='store_true', help='Force overwrite existing files.')
    parser.add_argument('--name', help='Name of the base Python module/package.')
    args = parser.parse_args()

    # Ask interactively if project name wasn't provided
    if not args.name:
        args.name = input("Enter your project module name (e.g., networksecurity): ").strip() or "project_name"

    # Replace 'project_name' with actual module name
    global DIR_STRUCTURE, FILE_STRUCTURE
    DIR_STRUCTURE = [p.replace("project_name", args.name) for p in DIR_STRUCTURE]
    FILE_STRUCTURE = [p.replace("project_name", args.name) for p in FILE_STRUCTURE]

    create_directories()
    create_files(force=args.force)
    create_init_files(base_package=f"src/{args.name}")
    print(f"✅ Project '{args.name}' structure created successfully.")

if __name__ == "__main__":
    main()
