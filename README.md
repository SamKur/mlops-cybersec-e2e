Reproducible Project Skeleton by Script (Once while creation of project)

```
python setup_project_skeleton.py
python setup_project_skeleton.py -f                         # WARNING: To skip prompts and overwrite all files
python setup_project_skeleton.py --name networksecurity -f  # Specify Project Folder Name
```

Create & Activate Virtual Environment & Install Deps

```
python -m venv .venv
source .venv/bin/activate               # Linux OR
.venv\Scripts\activate                  # Windows
pip install --upgrade pip setuptools wheel
pip install -e .                        # Install the requirements & enable editable import
pip freeze > requirements.txt           # Generate if needed
```

Run the package by
```
python -m networksecurity.main
python -m src.networksecurity.main   # if you're not in editable mode

```

Test utils etc by
```
python src/networksecurity/utils/exception.py
python -m src.networksecurity.utils.exception
```
