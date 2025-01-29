# testing basic gpt behaviour in python

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


client = OpenAI()

prompt="Tell me encouraging words about how well i am doing programming"
addendum="Answer in twenty words"

response = client.chat.completions.create(model="gpt-4o",
messages=[{"role": "user", "content": prompt + addendum}])

# Print each part of the response
if response.choices:
    for choice in response.choices:
        print(choice.message.content)
