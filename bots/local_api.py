import os
import subprocess

def load_zsh_and_get_api_key(key):
    # Command to source .zshrc and print the API_KEY environment variable
    command = 'source ~/.zshrc && echo ' + key 
    result = subprocess.run(['zsh', '-c', command], capture_output=True, text=True)

    if result.stdout:
        # print("API Key retrieved successfully:", result.stdout.strip())
        return result.stdout.strip()
    else:
        print("Failed to retrieve API Key. Error:", result.stderr.strip())
        return result.stderr.strip()

if __name__ == "__main__":
    # request = '$OPENAI_API_KEY'
    request = '$vincypt_http_api'
    key = load_zsh_and_get_api_key(request)
    print(f"The key for {request} is:\n {key}")
