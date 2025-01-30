import yaml
import os

# Define a function to load prompts from YAML and create a composed prompt
def create_prompt_from_yaml(yaml_file_path=None, active_modules=None):
    # Setup default path and modules if not provided
    if yaml_file_path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        yaml_file_path = os.path.join(base_dir, '../../prompts.yaml')
    
    if active_modules is None:
        active_modules = ("expert", 
                          "held-storytelling", 
                          "emojies", 
                          "project-title",
                          "held-jakob",
                          "held-self-organization",  
                          )

    # Load the YAML file
    with open(yaml_file_path, "r", encoding="utf-8") as file:
        prompt_modules = yaml.safe_load(file)

    # colors for text
    red_text = "\033[91m"
    reset_text_color = "\033[0m"

    # Create a prompt that combines specified modules
    prompt_composed = ""
    for module in active_modules:
        # Check if the module exists in prompt_modules
        if module in prompt_modules:
            prompt_composed += prompt_modules[module]['content']
        else:
            print(f"{red_text}Warning: '{module}' module not found in prompt_modules.{reset_text_color}")
    
    return prompt_composed

# If you want to test the function directly in this script
if __name__ == "__main__":
    # Create the prompt using defaults
    prompt = create_prompt_from_yaml()
    
    # For testing purposes, print the prompt
    print(prompt)