# Installation

To install the tool, run:

```bash
pip install .
```

# Usage

Generate an ASCII tree of the current directory with:

```bash
pytree
```

## Options:

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
```
