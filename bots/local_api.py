# this is a secure api key loader for the local api
# this works with systemd and also directly with python from the shell

import os
import subprocess

def load_shell_and_get_api_key(key):
    # Try using zsh first
    command = f"source ~/.zshrc && echo {key}"
    try:
        result = subprocess.run(['zsh', '-c', command], capture_output=True, text=True, check=True)
        if result.stdout:
            return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("zsh failed. Falling back to bash...")

    # Fallback to bash
    command = f"source ~/.bashrc && echo {key}"
    try:
        result = subprocess.run(['bash', '-c', command], capture_output=True, text=True, check=True)
        if result.stdout:
            return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Failed to retrieve API Key using both zsh and bash.")
        return None

if __name__ == "__main__":
    # Define the environment variable to fetch
    request = '$vincypt_http_api'
    key = load_shell_and_get_api_key(request)
    if key:
        print(f"The key for {request} is:\n{key}")
    else:
        print(f"Unable to retrieve the key for {request}.")