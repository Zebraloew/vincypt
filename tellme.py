#!/usr/bin/env python3
import sys
from openai import OpenAI

client = OpenAI()

# Assuming OPENAI_API_KEY is set in your environment variables.
# If not, uncomment and set your API key directly:
# openai.api_key = 'your_api_key_here'

# Check if at least one additional argument is provided
if len(sys.argv) > 1:
    input_text = " ".join(sys.argv[1:])  # Join all arguments into one string
    print("★")
    prompt = input_text + " Answer in at most twenty words. Add three emojis."
    
    try:
        # Note the updated method for creating completions
        response = client.completions.create(model="gpt-4",
        prompt=prompt,
        temperature=0.7,
        max_tokens=160,  # Adjust max tokens as needed
        n=1,
        stop=None)  # Define any stopping conditions, if necessary)
        # Print the text of the response
        print(response.choices[0].text.strip())
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("Please provide an input.")

# To make this script executable and callable from anywhere:
# 1. Make it executable: chmod +x tellme.py
# 2. Symlink it to a bin directory in your PATH, for example:
# sudo ln -s "/absolute/path/to/tellme.py" /usr/local/bin/tellme
""""
chmod +x tellme.py && sudo ln -s "/Users/zebralow/Library/Mobile Documents/com~apple~CloudDocs/jCloud Drive/codecloud/gpt/tellme.py" /usr/local/bin/tellme

"""