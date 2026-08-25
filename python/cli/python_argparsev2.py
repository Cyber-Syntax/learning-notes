import argparse
from pathlib import Path


def directory(value: str) -> Path:
    """Check directory and return as Path."""
    path = Path(value)

    if not path.is_dir():
        message = f"'{value}' is not a directory"
        raise argparse.ArgumentTypeError(message)

    return path


parser = argparse.ArgumentParser()

parser.add_argument(
    "path",
    type=directory,
    metavar="DIRECTORY",
)

args = parser.parse_args()

for entry in args.path.iterdir():
    print(entry.name)
