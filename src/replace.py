import re
import os
import json

def find_and_replace_files():
    pattern = os.getenv('pattern')
    directory = os.getenv('directory')
    replacements_json = os.getenv('replacements_json')
    
    replacements = json.loads(replacements_json)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if re.search(pattern, file_path):
                print(f"File found:", file_path)
                with open(file_path, 'r') as f:
                    content = f.read()
                replaced = False
                for rep in replacements:
                    match = re.search(rep['regex'], content)
                    if match:
                        replaced = True
                        matched_string = match.group()
                        print(f"Matched regex:", matched_string)
                        replacement = rep['replacement']
                        print(f"Replacement string:", replacement)
                        content = re.sub(rep['regex'], replacement, content)
                if not replaced:
                    print(f"No regex matches found.")
                with open(file_path, 'w') as f:
                    f.write(content)

# Execute the function
if __name__ == "__main__":
    find_and_replace_files()
