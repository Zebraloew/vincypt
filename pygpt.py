# testing basic gpt behaviour in python

from openai import OpenAI

client = OpenAI()

prompt="What is a good prompt?"
addendum="Answer in twenty words"

response = client.chat.completions.create(model="gpt-4",
messages=[{"role": "user", "content": prompt + addendum}])

# Print each part of the response
if response.choices:
    for choice in response.choices:
        print(choice.message['content'])
