#!/opt/venvs/gpt_env/bin/python

import yaml
import os

# Construct an absolute path for the YAML file
base_dir = os.path.dirname(os.path.abspath(__file__))
yaml_file_path = os.path.join(base_dir, 'prompts.yaml')

# YAML file
with open(yaml_file_path, "r", encoding="utf-8") as file:
    prompt_modules = yaml.safe_load(file)

# colors for text
red_text = "\033[91m"
reset_text_color = "\033[0m"

# Create a prompt that combines some modules
active_prompt_modules = ("expert", "wirk-activist", "emojies")
prompt_composed = ""
for module in active_prompt_modules:
    # Check if the module exists in prompt_modules
    if module in prompt_modules:
        prompt_composed += prompt_modules[module]['content']
    else:
        print(f"{red_text}Warning: '{module}' module not found in prompt_modules.{reset_text_color}")

prompt = prompt_composed

print(prompt)