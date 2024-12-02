import os
import argparse
import subprocess

def generate_directory_tree(path, exclude_cache=True, max_depth=None):
    branch, tee, last = "├── ", "│   ", "└── "
    tree_lines = []

    def traverse_directory(directory_path, prefix="", current_depth=0):
        if max_depth is not None and current_depth >= max_depth:
            return

        contents = sorted(os.listdir(directory_path))
        contents = [
            item for item in contents if not (
                item == "__pycache__" or item.endswith(".pyc") or 
                item == ".gitignore" or item.endswith(".db") or item.endswith(".log")
            )
        ]
        contents = [
            item for item in contents if os.path.isdir(os.path.join(directory_path, item)) or os.path.isfile(os.path.join(directory_path, item))
        ]

        for index, item_name in enumerate(contents):
            full_path = os.path.join(directory_path, item_name)
            connector = last if index == len(contents) - 1 else branch
            tree_lines.append(f"{prefix}{connector}{item_name}")
            if os.path.isdir(full_path):
                new_prefix = prefix + (tee if index != len(contents) - 1 else "    ")
                traverse_directory(full_path, new_prefix, current_depth + 1)

    tree_lines.append(f"[{os.path.basename(path)}]")
    traverse_directory(path)
    return "\n".join(tree_lines)

def copy_text_to_clipboard(text):
    try:
        process = subprocess.Popen('clip', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        process.communicate(input=text.encode('utf-16'))
    except Exception as error:
        print(f"Copy error: {error}")

def main():
    parser = argparse.ArgumentParser(description="Generate directory tree and copy to clipboard.")
    parser.add_argument("path", type=str, nargs="?", default=os.getcwd(), help="Directory path (default: current).")
    parser.add_argument("--exclude-cache", action="store_true", help="Exclude cache files/folders.")
    parser.add_argument("--max-depth", type=int, default=None, help="Limit the depth of the tree.")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Invalid path: '{args.path}'")
        return

    directory_tree = generate_directory_tree(args.path, args.exclude_cache, args.max_depth)
    print(directory_tree)
    copy_text_to_clipboard(directory_tree)
    print("Tree copied to clipboard.")

if __name__ == "__main__":
    main()
