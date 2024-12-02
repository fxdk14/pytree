# Install the tool
pip install .

# Generate an ASCII tree of the current directory
pytree

# Options:
pytree --exclude-cache       # Exclude cache files
pytree --max-depth [number]  # Limit tree depth

# Example Output
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
