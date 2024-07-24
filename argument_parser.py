import argparse

parser = argparse.ArgumentParser()

# Positional arguments
parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("square", help="display a square of a given number",
                    type=int)

# Optional arguments
parser.add_argument("--verbosity", help="increase output verbosity")
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    default=0,
                    help="increase output verbosity")

# nargs
parser.add_argument('-n', nargs='+')
parser.add_argument('args', nargs='*')

args = parser.parse_args()

print(args)