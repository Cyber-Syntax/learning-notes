"""python argparse library example."""

import argparse
from pathlib import Path

# The object responsible for understanding the arguments my program accepts
parser = argparse.ArgumentParser()

# My program requires one positional argument, and I'm going to call it path
#
# Now we can use args.path to access that argument
#
# NOTE: instead of using sys.argv[1], this know directly get
# the argument called "path"
#
# layout: `python_argparse.py PATH`
# example args mean `src` -> `python python_argparse.py src`
#
# metavar gives useful name in help instead of showing path:
# usage: python_argparse.py [-h] DIRECTORY
#
# instead of :
# usage: python_argparse.py [-h] path
parser.add_argument("path", type=Path, metavar="DIRECTORY")


# example: `python python_argparse.py src`
#
# parse_args() read the command line and says:
# The user provided "src".
# The program says it expects an argument called "path"
# Therefore:
#   path = "src"
# so:
# args.path = "src"
args = parser.parse_args()

# # get the target_dir via args.path
# # Example:
# # target_dir = Path(args.path)
# # target_dir = Path("src")
# # target_dir = "src"
# target_dir = Path(args.path)
#
# We don't need Path anymore which we gave type=path in add_argument
# target_dir = args.path

if not args.path.is_dir():
    print(f"Error: '{args.path}' is not a directory")
    raise SystemExit(1)

for entry in args.path.iterdir():
    print(entry.name)
