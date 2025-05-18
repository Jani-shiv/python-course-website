import os

# Define folders to create
folders = [
    "beginner",
    "intermediate/oop",
    "advanced",
    "projects/calculator",
    "projects/todo_app",
    "projects/guess_number",
    "assets/css",
    "assets/js",
    "assets/images",
    "assets/notes",
]

# Define files to create with their relative paths
files = [
    # Beginner files
    "beginner/comments.html",
    "beginner/variables.html",
    "beginner/data_types.html",
    "beginner/operators.html",
    "beginner/input_output.html",
    "beginner/strings.html",
    "beginner/lists.html",
    "beginner/tuples.html",
    "beginner/dictionaries.html",
    "beginner/sets.html",
    "beginner/conditionals.html",
    "beginner/loops.html",
    "beginner/functions.html",
    "beginner/modules.html",
    "beginner/exceptions.html",

    # Intermediate files
    "intermediate/file_io.html",
    "intermediate/list_comprehensions.html",
    "intermediate/lambda_map_filter.html",
    "intermediate/recursion.html",
    "intermediate/modules_packages.html",
    "intermediate/errors_exceptions.html",
    "intermediate/oop/classes.html",
    "intermediate/oop/inheritance.html",
    "intermediate/oop/polymorphism.html",

    # Advanced files
    "advanced/decorators.html",
    "advanced/generators.html",
    "advanced/context_managers.html",
    "advanced/threading.html",
    "advanced/asyncio.html",
    "advanced/metaprogramming.html",
    "advanced/testing.html",
    "advanced/performance.html",

    # Projects files
    "projects/calculator/index.html",
    "projects/calculator/main.py",
    "projects/todo_app/index.html",
    "projects/todo_app/main.py",
    "projects/guess_number/index.html",
    "projects/guess_number/main.py",

    # Assets files
    "assets/css/styles.css",
    "assets/js/skulpt.min.js",
    "assets/js/skulpt-stdlib.js",
    "assets/js/app.js",
    "assets/images/placeholder.png",
    "assets/notes/beginner_guide.pdf",
    "assets/notes/intermediate_guide.pdf",
    "assets/notes/advanced_guide.pdf",
]

def create_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    for file_path in files:
        # Create empty file only if it doesn't exist
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                pass
            print(f"Created file: {file_path}")
        else:
            print(f"File already exists: {file_path}")

if __name__ == "__main__":
    create_structure()
    print("All folders and files created successfully!")
