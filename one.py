import os
import sys

def apply_patch():
    try:
        import pkg_resources
    except ImportError:
        print("pkg_resources is not installed.")
        return

    # Find the __init__.py file of pkg_resources
    pkg_resources_path = os.path.join(
        os.path.dirname(pkg_resources.__file__), '__init__.py'
    )

    # Read the content of the file
    with open(pkg_resources_path, 'r') as file:
        lines = file.readlines()

    # Apply the patch by commenting out the specific line
    with open(pkg_resources_path, 'w') as file:
        for line in lines:
            if 'pkgutil.ImpImporter' in line:
                file.write(f'# {line}')
            else:
                file.write(line)

    print(f"Patched {pkg_resources_path}")

if __name__ == "__main__":
    apply_patch()
    print("Patch applied. You can now run your script.")
