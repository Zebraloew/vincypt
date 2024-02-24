#!/usr/bin/env python3
import argparse
import openai

# Assuming you have set your OPENAI_API_KEY in your environment variables,
# otherwise, you can set it directly in your script as follows:
# openai.api_key = 'your_api_key_here'

### To make it work in the Terminal
### Further instructions on the bottom

# Create the parser
parser = argparse.ArgumentParser(description="Process some inputs.")
# Add arguments
parser.add_argument('-i', '--input', help='Input prompt')
# Parse the arguments
args = parser.parse_args()

# Use the input
print(f"Received input: {args.input}")


prompt = args.input
addendum = ". Answer in twenty words. Add three emojies."

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt + addendum}]
)

# Print each part of the response
if response.choices:
    for choice in response.choices:
        print(choice.message['content'])



"""

chmod +x tellme.py && sudo ln -s "/Users/zebralow/Library/Mobile Documents/com~apple~CloudDocs/jCloud Drive/codecloud/gpt/tellme.py" /usr/local/bin/tellme

"""
