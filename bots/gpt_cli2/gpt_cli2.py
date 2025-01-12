#!/opt/venvs/gpt_env/bin/python

from argparse import ArgumentParser
from db_utils import get_db_connection, ensure_table_exists
from chat_utils import chat_with_gpt

def main():
    parser = ArgumentParser(description="GPT Command Line Interface")
    parser.add_argument("input", nargs="+", help="Input message for GPT")
    args = parser.parse_args()

    input_text = " ".join(args.input)

    # Connect to the database
    conn = get_db_connection()
    ensure_table_exists(conn)

    # Chat with GPT
    reply = chat_with_gpt(conn, input_text)
    print(reply)

if __name__ == "__main__":
    main()