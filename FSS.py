class Node:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []  # Only for directories

    def find_child(self, name):
        return next((child for child in self.children if child.name == name), None)

    def is_empty(self):
        return len(self.children) == 0


class FileSystem:
    def __init__(self):
        self.root = Node("root")

    def find_node(self, path):
        parts = path.strip("/").split("/")
        current = self.root
        for part in parts:
            if part == "":
                continue
            current = current.find_child(part)
            if current is None:
                return None
        return current

    def mkdir(self, path):
        parent_path, dir_name = "/".join(path.split("/")[:-1]), path.split("/")[-1]
        parent = self.find_node(parent_path) if parent_path else self.root
        if parent is None or parent.is_file:
            print(f"Error: Invalid directory path '{path}'.")
            return
        if parent.find_child(dir_name):
            print(f"Error: Directory '{dir_name}' already exists.")
            return
        parent.children.append(Node(dir_name))
        print(f"Directory '{dir_name}' created.")

    def add(self, path):
        parent_path, file_name = "/".join(path.split("/")[:-1]), path.split("/")[-1]
        parent = self.find_node(parent_path) if parent_path else self.root
        if parent is None or parent.is_file:
            print(f"Error: Invalid directory path '{path}'.")
            return
        if parent.find_child(file_name):
            print(f"Error: File '{file_name}' already exists.")
            return
        parent.children.append(Node(file_name, is_file=True))
        print(f"File '{file_name}' added.")

    def search(self, name):
        result = self._search_recursive(self.root, name, "")
        if result:
            print(f"File found in: {result}")
        else:
            print(f"Error: '{name}' not found.")

    def _search_recursive(self, current, name, path):
        if current.name == name:
            return f"{path}/{current.name}"
        for child in current.children:
            result = self._search_recursive(child, name, f"{path}/{current.name}")
            if result:
                return result
        return None

    def ls(self, path):
        directory = self.find_node(path)
        if directory is None or directory.is_file:
            print(f"Error: Directory '{path}' does not exist.")
            return
        for child in directory.children:
            print(child.name)

    def rm(self, path):
        parent_path, name = "/".join(path.split("/")[:-1]), path.split("/")[-1]
        parent = self.find_node(parent_path) if parent_path else self.root
        if parent is None or parent.is_file:
            print(f"Error: Invalid directory path '{path}'.")
            return
        node = parent.find_child(name)
        if node is None:
            print(f"Error: '{name}' does not exist.")
            return
        if not node.is_file and not node.is_empty():
            print(f"Error: Directory '{name}' is not empty.")
            return
        parent.children.remove(node)
        print(f"'{name}' removed.")

    def mv(self, src_path, dest_path):
        src_parent_path, src_name = "/".join(src_path.split("/")[:-1]), src_path.split("/")[-1]
        src_parent = self.find_node(src_parent_path) if src_parent_path else self.root
        dest = self.find_node(dest_path)

        if src_parent is None or src_parent.is_file or dest is None or dest.is_file:
            print(f"Error: Invalid source or destination path.")
            return
        node = src_parent.find_child(src_name)
        if node is None:
            print(f"Error: '{src_name}' does not exist.")
            return
        if dest.find_child(src_name):
            print(f"Error: '{src_name}' already exists in the destination.")
            return
        src_parent.children.remove(node)
        dest.children.append(node)
        print(f"'{src_name}' moved to '{dest_path}'.")

    def tree(self, node=None, prefix=""):
        node = node or self.root
        print(f"{prefix}{node.name}")
        for child in node.children:
            self.tree(child, prefix + "  ")

    def execute_command(self, command):
        args = command.split()
        if not args:
            return
        cmd = args[0]
        if cmd == "mkdir" and len(args) == 2:
            self.mkdir(args[1])
        elif cmd == "add" and len(args) == 2:
            self.add(args[1])
        elif cmd == "search" and len(args) == 2:
            self.search(args[1])
        elif cmd == "ls" and len(args) == 2:
            self.ls(args[1])
        elif cmd == "rm" and len(args) == 2:
            self.rm(args[1])
        elif cmd == "mv" and len(args) == 3:
            self.mv(args[1], args[2])
        elif cmd == "tree" and len(args) == 1:
            self.tree()
        else:
            print(f"Error: Invalid command '{command}'.")


if __name__ == "__main__":
    fs = FileSystem()
    print("Enter commands (type 'exit' to quit):")
    while True:
        command = input("> ").strip()
        if command == "exit":
            break
        fs.execute_command(command)
