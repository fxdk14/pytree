# Installation

Run `setup.bat` to install:

```bash
> setup.bat
```

# Usage

Generate an ASCII tree of the current directory with:

```bash
> pytree
```

## Options:
- ```path``` : Directory to generate the tree (default: current).
- ```--exclude-cache``` : Exclude cache files from the tree.
- ```--max-depth [number]``` : Limit the tree depth.

# Example Output

```plaintext
[Project]
├── src
│   ├── app.py
│   └── utils
│       ├── logger.py
│       └── parser.py
├── tests
│   ├── test_app.py
│   └── test_utils.py
├── README.md
└── requirements.txt
Tree copied to clipboard.
```
