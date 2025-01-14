# This is just testing the argparse function for a shell script

#!/usr/bin/env python3
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Process some inputs.")

# Add arguments
parser.add_argument('-i', '--input', help='Input prompt')

# Parse the arguments
args = parser.parse_args()

# Use the input
print(f"Received input: {args.input}")


"""
chmod +x testargparse
sudo ln -s "/Users/zebralow/Library/Mobile Documents/com~apple~CloudDocs/jCloud Drive/codecloud/gpt/testargparse.py" /usr/local/bin/testargparse




"""