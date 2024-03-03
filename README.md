# replace-in-files
Github action to replace multiple strings within files using regex.

# Example usage
```
- name: Custom Python Search and Replace
    uses: carefreepineapple/replace-in-files@main
    with:
        directory: '${{ github.workspace }}'
        file_pattern: '^test_file.*\.txt$'
        replacements_json: |
        [
            {"regex": "test", "replacement": "exam"},
            {"regex": "This", "replacement": "that"},
            {"regex": "file \\d+", "replacement": "file new number"}
        ]
```

# Example workflow
This repo uses an example workflow. https://github.com/carefreepineapple/replace-in-files/actions