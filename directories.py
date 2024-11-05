from typing import Tuple, Optional, Dict, List
import sys

class DirNode:
    """Represents a directory node in the directory tree."""
    def __init__(self, name: str):
        self.name: str = name
        self.children: Dict[str, 'DirNode'] = {}

class DirectoryTree:
    """Manages directory operations such as CREATE, MOVE, DELETE, and LIST."""
    def __init__(self):
        self.root = DirNode('')  

    def create(self, path: str) -> None:
        """Creates directories along the specified path."""
        if not path:
            print("Error: Path cannot be empty.")
            return
        parts = path.strip('/').split('/')
        current = self.root
        for part in parts:
            if not part:
                print("Error: Invalid directory name.")
                return
            if part not in current.children:
                current.children[part] = DirNode(part)
            current = current.children[part]

    def find_node(self, path: str) -> Tuple[Optional[DirNode], Optional[str]]:
        """Finds the node at the specified path.

        Returns:
            Tuple[DirNode or None, str or None]: Returns the node if found, else None.
            Also returns the first missing part if the path does not exist.
        """
        if not path:
            return None, "Path cannot be empty."
        parts = path.strip('/').split('/')
        current = self.root
        for part in parts:
            if not part:
                return None, "Invalid directory name."
            if part in current.children:
                current = current.children[part]
            else:
                return None, part  
        return current, None

    def find_node_and_parent(self, path: str) -> Tuple[Optional[DirNode], Optional[DirNode], Optional[str]]:
        """Finds the node and its parent at the specified path.

        Returns:
            Tuple[Parent DirNode or None, Target DirNode or None, Missing part or None]
        """
        if not path:
            return None, None, "Path cannot be empty."
        parts = path.strip('/').split('/')
        current = self.root
        parent = None
        for part in parts:
            if not part:
                return None, None, "Invalid directory name."
            if part in current.children:
                parent = current
                current = current.children[part]
            else:
                return None, None, part 
        return parent, current, None

    def move(self, source_path: str, dest_path: str) -> None:
        """Moves a directory from source_path to dest_path."""
        if not source_path or not dest_path:
            print("Error: Source and destination paths cannot be empty.")
            return
        source_parent, source_node, source_missing = self.find_node_and_parent(source_path)
        if source_missing:
            print(f'Cannot move {source_path} - {source_missing} does not exist')
            return
        if source_node is None or source_parent is None:
            print(f'Cannot move {source_path} - {source_path} does not exist')
            return
        dest_node, dest_missing = self.find_node(dest_path)
        if dest_missing:
            print(f'Cannot move {source_path} - {dest_missing} does not exist')
            return
        if dest_node is None:
            print(f'Cannot move {source_path} - {dest_path} does not exist')
            return
        if self.is_subdirectory(source_node, dest_node):
            print(f'Cannot move {source_path} - cannot move a directory inside itself')
            return
        del source_parent.children[source_node.name]
        dest_node.children[source_node.name] = source_node

    def delete(self, path: str) -> None:
        """Deletes the directory at the specified path."""
        if not path:
            print("Error: Path cannot be empty.")
            return
        parent_node, target_node, missing_part = self.find_node_and_parent(path)
        if missing_part:
            print(f'Cannot delete {path} - {missing_part} does not exist')
            return
        if target_node is None or parent_node is None:
            print(f'Cannot delete {path} - {path} does not exist')
            return
        del parent_node.children[target_node.name]

    def list(self) -> None:
        """Prints the directory tree structure."""
        self._print_tree(self.root, 0)

    def _print_tree(self, node: DirNode, depth: int) -> None:
        """Recursively prints the directory tree."""
        for name in sorted(node.children.keys()):
            print('  ' * depth + name)
            self._print_tree(node.children[name], depth + 1)

    def is_subdirectory(self, source_node: DirNode, dest_node: DirNode) -> bool:
        """Checks if dest_node is a subdirectory of source_node."""
        if source_node == dest_node:
            return True
        for child in source_node.children.values():
            if self.is_subdirectory(child, dest_node):
                return True
        return False

def parse_command(command_line: str) -> Tuple[str, List[str]]:
    parts = command_line.strip().split()
    command = parts[0]
    args = parts[1:]
    return command, args

def process_command(command_line: str, directory_tree: DirectoryTree) -> None:
    """Processes a single command."""
    command_line = command_line.strip()
    if not command_line:
        return
    try:
        command, args = parse_command(command_line)
        if command == 'CREATE':
            if len(args) != 1:
                print("Error: CREATE command requires one argument.")
                return
            path = args[0]
            directory_tree.create(path)
        elif command == 'MOVE':
            if len(args) != 2:
                print("Error: MOVE command requires two arguments.")
                return
            source_path, dest_path = args
            directory_tree.move(source_path, dest_path)
        elif command == 'DELETE':
            if len(args) != 1:
                print("Error: DELETE command requires one argument.")
                return
            path = args[0]
            directory_tree.delete(path)
        elif command == 'LIST':
            directory_tree.list()
        else:
            print(f'Unknown command: {command}')
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Reads commands from standard input or a file and processes each command."""
    directory_tree = DirectoryTree()
    if len(sys.argv) > 1:
        # Input text file provided
        input_file = sys.argv[1]
        try:
            with open(input_file, 'r') as f:
                commands = f.readlines()
            for command_line in commands:
                process_command(command_line, directory_tree)
        except FileNotFoundError:
            print(f"File not found: {input_file}")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
    else:
        # Read from standard input
        try:
            while True:
                command_line = input()
                process_command(command_line, directory_tree)
        except EOFError:
            pass
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()

