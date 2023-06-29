import os


def load_env(file):
    """Load environment variables from a .env file."""
    with open(file) as f:
        for line in f:
            key, value = line.strip().split("=", 1)
            # if value is suronded by "" or '' then remove them
            if value[0] == value[-1] == '"' or value[0] == value[-1] == "'":
                value = value[1:-1]
            os.environ.setdefault(key, value)
