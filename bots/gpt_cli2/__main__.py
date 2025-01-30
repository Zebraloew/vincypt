#!/opt/venvs/gpt_env/bin/python

# to do 
# add a prime prompt from prompt gen as first message

from argparse import ArgumentParser
from db_utils import get_db_connection, ensure_table_exists
from chat_utils import chat_with_gpt

import textwrap

def main():
    # Parse command-line arguments in shell like: 
    # > python gpt_cli2.py "Hello, how are you?"
    parser = ArgumentParser(description="GPT Command Line Interface")
    parser.add_argument("input", nargs="+", help="Input message for GPT")
    args = parser.parse_args()

    input_text = " ".join(args.input)

    # Connect to the database
    conn = get_db_connection()
    ensure_table_exists(conn)

    # Print reply with GPT
    reply = chat_with_gpt(conn, input_text)
    # turquoise color text intro 
    print("\033[1;36m\n𓂀  \033[0m", end=" ")
    # wrap the text to make it look nicer
    print(textwrap.fill(reply, width=80))

if __name__ == "__main__":
    main()