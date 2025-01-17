import json

with open("prompt_modules.json", "r") as file:
    prompt_modules = json.load(file)

# create a prompt that combines some modules
active_prompt_modules=("expert","wirk-activist","emojies")
promptpecomposed=""
for module in active_prompt_modules:
    promptpecomposed+=prompt_modules[module]    

prompt=promptpecomposed

print(prompt)