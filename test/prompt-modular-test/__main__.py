import json

# colors for text
red_text="\033[91m" 
reset_text_color="\033[0m" 

# Create a prompt that combines some modules
active_prompt_modules = ("expert", "wirk-activist", "emojiesy")
prompt_composed = ""
for module in active_prompt_modules:
    # Check if the module exists in prompt_modules
    if module in prompt_modules:
        prompt_composed += prompt_modules[module]
    else:
        print(f"{red_text}Warning: '{module}' module not found in prompt_modules.{reset_text_color})")

prompt = prompt_composed

print(prompt)