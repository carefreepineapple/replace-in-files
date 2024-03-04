# disclaimer
ChatGPT wrote this, I just provided guidance, testing, and minor bug fixes.  How does that affect the MIT license?  No clue, welcome to the wild west!

# replace-in-files
Github action to replace multiple strings within files using regex.

# usage notes
## debug
the debug flag has a default setting of false, so it does not need to be specified except when `true`.  When set to `true`, it will print the original and modified contents of the files that have matching content.

## recursive
the recursive flag has a default setting of `true`, so it will recursively search through child directories, within the specified directory, for matching files.  Set this to `false` if you do not want a recursive search.

## regex notes
be mindful as its needed to escape the escape, ie. you want to escape an underscore: `\\_`

# example usage
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
        recursive: true
```

# example workflow
This repo uses an example workflow. https://github.com/carefreepineapple/replace-in-files/actions