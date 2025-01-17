import json

with open("prompt_modules.json", "r") as file:
    prompt_modules = json.load(file)


prompt="OH HAI\n You look great today!"+prompt_modules["personality-vincy"]+prompt_modules["expert"]+prompt_modules["emojies"]
print(prompt)