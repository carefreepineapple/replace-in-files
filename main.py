import os
import re
import json

def main():
    directory = os.getenv('DIRECTORY')
    file_pattern = os.getenv('FILE_PATTERN')
    replacements_json = os.getenv('REPLACEMENTS_JSON')

    print(f"Directory: {directory}")
    print(f"File Pattern: {file_pattern}")
    print(f"Replacements JSON: {replacements_json}")

    try:
        if replacements_json:
            replacements_data = json.loads(replacements_json)

            if not isinstance(replacements_data, list):
                raise ValueError("Replacements data must be a list")

        for file_name in os.listdir(directory):
            if re.match(file_pattern, file_name):
                file_path = os.path.join(directory, file_name)
                print(f"File matched: {file_path}")

                if replacements_json:
                    with open(file_path, 'r') as f:
                        content = f.read()

                    modified_content = content  # Initialize modified content

                    for rep in replacements_data:
                        regex = rep.get('regex')
                        replacement = rep.get('replacement')
                        if regex and replacement:
                            modified_content = re.sub(regex, replacement, modified_content)

                    if modified_content != content:  # Check if content was replaced
                        print(f"Content found and replaced in {file_name}")

                        with open(file_path, 'w') as f:
                            f.write(modified_content)

                        print(f"Modified contents of {file_name}:")
                        print(modified_content)
                    else:
                        print(f"No content replaced in {file_name}")

                else:
                    print("No replacements provided.")
    except Exception as e:
        print(f"Error processing replacements: {e}")

if __name__ == "__main__":
    main()
