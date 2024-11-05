# Directory Management

## Files Included

- `directories.py`: The main Python script containing the implementation of the directory tree management system.
- `input.txt`: A text file containing a set of commands to be executed by the program.
- `test_directories.py`: A Python script containing unit tests for the `DirectoryTree` class.

## How to Run

### Running the Program with Standard Input

You can run the program and enter commands manually:

```bash
python directories.py
```

Then, input the commands line by line. For example:

```
CREATE fruits
CREATE fruits/apples
LIST
```

### Running the Program with an Input File

You can also run the program using commands from a file (e.g., `input.txt`):

```bash
python directories.py input.txt
```

Note: Ensure that input.txt is in the same folder as directories.py.
The program will read commands from the specified file and execute them accordingly.

## Running Tests

To execute the unit tests provided in test_directories.py, make sure the test file is in the same folder as directories.py, then run:

```bash
python test_directories.py
```

This will run all the test cases to ensure that the `DirectoryTree` class functions as expected.

## Implementation Details

- **`directories.py`**: Contains the implementation of the `DirectoryTree` and `DirNode` classes, as well as functions to parse and process commands.
  - **`DirNode`**: Represents a node in the directory tree.
  - **`DirectoryTree`**: Manages directory operations and maintains the tree structure.
  - **Command Processing**: The `process_command` function parses and executes each command.
  - **Error Handling**: The program includes error messages for invalid operations, matching the expected output.
- **Assumptions**:
- Directory name and commands are case-sensitive.
- The program simulates the directory structure in memory and does not interact with the actual filesystem.
