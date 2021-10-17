# madlib-cli

## Description

* This program simulates Mad Libs game which is a typical word game that consists of one player who asks the others for a list of words to fill in the blanks in the story before reading out loud.

## **Live PR URL** [link](https://github.com/BasharTaamneh/madlib-cli/pull/1)

## Requirment

```javascript
poetry
python 3.9.7
pytest
```

## Getting started

```bash
poytry install
poetry shell
pytest
python -m Modules_and_Testing.math_series
```

**Collaboratores:**

* The whole class.

## This madlib-cli

* [x] Print a welcome message to the user, explaining the Madlib process and command line interactions.

* [x] Read a template Madlib file (Example), and parse that file into usable parts.

* [x] Prompt the user to submit a series of words to fit each of the required components of the Madlib template.

* [x] With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.

* [x] After the resulting Madlib has been completed, provide the completed response back to the user in the command line.

* [x] Write the completed text (Example)to a new file on your file system (in the repo).

## Testing Details

* [x] Create and test a read_template function that takes in a path to text file and returns a stripped string of the file’s contents.

* [x] read_template should raise a FileNotFoundError if path is invalid.

* [x] Create and test a parse_template function that takes in a template string and returns a string with language parts removed and a separate list of those language parts.

* [x] Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
