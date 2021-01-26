# arg parser
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, default=None, required=False, help='test')
args = parser.parse_args()

print(args.file)