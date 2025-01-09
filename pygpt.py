from openai import OpenAI

client = OpenAI()

# Assuming you have set your OPENAI_API_KEY in your environment variables,
# otherwise, you can set it directly in your script as follows:
# openai.api_key = 'your_api_key_here'

prompt="What is a good prompt?"
addendum="Answer in twenty words"

response = client.chat.completions.create(model="gpt-4",
messages=[{"role": "user", "content": prompt + addendum}])

# Print each part of the response
if response.choices:
    for choice in response.choices:
        print(choice.message['content'])
