#!/Users/zebralow/openai-env/bin/python3
# shebang line to specify the python interpreter to use

# description
# this is a gpt that is accessed via the terminal locally

import sys
from openai import OpenAI

client = OpenAI()

# Check if at least one additional argument is provided
input_text = ""
if len(sys.argv) > 1:
    input_text = " ".join(sys.argv[1:])  # Join all arguments into one string
    print(f"★")
else:
    print("Please provide an input.")


### To make it work in the Terminal
### Further instructions on the bottom


prompt = input_text
addendum = ". Answer in at most twenty words. Add three emojies."

try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt + addendum}],
        temperature=0.9,
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


# this enables the use of the script in the terminal
# just type tellme and then your input in the terminal
"""
chmod +x tellme.py && \
sudo rm /usr/local/bin/tellme && \
sudo ln -s "$(pwd)/tellme.py" /usr/local/bin/tellme

"""
  