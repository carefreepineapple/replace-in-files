# disclaimer
ChatGPT wrote this, I just provided guidance, testing, and minor bug fixes.  How does that affect the MIT license?  No clue, welcome to the wild west!

# replace-in-files
Github action to replace multiple strings within files using regex.

# Example usage
the debug flag has a default setting of false.  When set to `true`, it will print the original and modified contents of the files that have matching content.
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
        debug: true
```

# Example workflow
This repo uses an example workflow. https://github.com/carefreepineapple/replace-in-files/actions