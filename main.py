import os
import re
import json

def main():
    directory = os.getenv('DIRECTORY')
    file_pattern = os.getenv('FILE_PATTERN')
    replacements_json = os.getenv('REPLACEMENTS_JSON')
    debug_mode = os.getenv('DEBUG') == 'true'
    recursive_search = os.getenv('RECURSIVE_SEARCH') == 'true'  # New flag for recursive search

    print(f"Directory: {directory}")
    print(f"File Pattern: {file_pattern}")
    print(f"Replacements JSON: {replacements_json}")
    print(f"Recursive Search: {recursive_search}")

    try:
        if replacements_json:
            replacements_data = json.loads(replacements_json)

            if not isinstance(replacements_data, list):
                raise ValueError("Replacements data must be a list")

        if recursive_search:
            for root, _, files in os.walk(directory):
                for file_name in files:
                    if re.match(file_pattern, file_name):
                        file_path = os.path.join(root, file_name)
                        process_file(file_path, replacements_data, debug_mode)
        else:
            for file_name in os.listdir(directory):
                if re.match(file_pattern, file_name):
                    file_path = os.path.join(directory, file_name)
                    process_file(file_path, replacements_data, debug_mode)
    except Exception as e:
        print(f"Error processing replacements: {e}")

def process_file(file_path, replacements_data, debug_mode):
    print(f"File matched: {file_path}")

    if debug_mode:
        print(f"Original contents of {os.path.basename(file_path)}:")
        with open(file_path, 'r') as f:
            content = f.read()
            print(content)

    if replacements_data:
        with open(file_path, 'r') as f:
            content = f.read()
        modified = False
        for rep in replacements_data:
            regex = rep.get('regex')
            replacement = rep.get('replacement')
            if regex and replacement:
                replaced_content, count = re.subn(regex, replacement, content)
                if count > 0:
                    modified = True
                    content = replaced_content

        if modified and not debug_mode:
            print(f"Content was found and replaced in: {os.path.basename(file_path)}")

        if debug_mode:
            print(f"Modified contents of {os.path.basename(file_path)}:")
            print(content)

        with open(file_path, 'w') as f:
            f.write(content)
    else:
        print("No replacements provided.")

if __name__ == "__main__":
    main()
