#!/usr/bin/env python3
import sys
from openai import OpenAI

client = OpenAI()

# Check if at least one additional argument is provided
input_text = ""
if len(sys.argv) > 1:
    input_text = " ".join(sys.argv[1:])  # Join all arguments into one string
    print(f"★")
    # Your logic here to process the input_text
else:
    print("Please provide an input.")

# Assuming you have set your OPENAI_API_KEY in your environment variables,
# otherwise, you can set it directly in your script as follows:
# openai.api_key = 'your_api_key_here'

### To make it work in the Terminal
### Further instructions on the bottom


prompt = input_text
addendum = ". Answer in at most twenty words. Add three emojies."

try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt + addendum}],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    # Print each part of the response
    if response.choices:
        for choice in response.choices:
            print(choice.message.content)

except Exception as e:
    print(f"An error occurred: {e}")


"""

chmod +x tellme.py && sudo ln -s "/Users/zebralow/Library/Mobile Documents/com~apple~CloudDocs/jCloud Drive/codecloud/gpt/tellme.py" /usr/local/bin/tellme

"""
