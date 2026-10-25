from pathlib import Path
from advanced_rag import (build_rag,retrieve)
from generator import ( generate_answer)
from dotenv import load_dotenv
import os
from sql_result import run_sql_from_generator
import psycopg2

# loading environment into python program
load_dotenv()


# Connect to PostgreSQL
conn = psycopg2.connect(
       dbname="postgres",
       user="postgres",
       password="tiger",
       host="localhost",
       port="5432"
        )

# Create a cursor
cur = conn.cursor()

#DOCUMENT_PATH = ( Path("Documents")
#                    / "*.txt")
# The path from which it will build RAG
DOCUMENT_PATH = Path("Documents")
txt_files = DOCUMENT_PATH.glob("*.txt")

def main():

    # Read all .txt files in Documents
    for file in DOCUMENT_PATH.glob("*.txt"):
        text = file.read_text(encoding="utf-8")
    print("Building RAG knowledge base...")

    build_rag(
        text,
        DOCUMENT_PATH.name
    )

    print(
        "\nAdvanced RAG is ready."
    )

    while True:

        query = input(
            "\nYou : "
        ).strip()

        print(query)

        if query.lower() in {
            "exit",
            "quit"
        }:
            break

        results = retrieve(
            query,
            top_k=5
        )

        print(
            "\nRetrieved Sources Ranking:"
        )

        for result in results:

            print(
                f"- "
                f"{result['source']} "
                f"(chunk "
                f"{result['chunk_id']})"
            )
        print(results)

        answer = generate_answer(query,results)
        # Print the results
        

        print("\nRAG :")

        print(answer)
        #print("Database Results:")
        ROWS = run_sql_from_generator(query,results)
        print(ROWS)
        
        #print("ROWS")
       

if __name__ == "__main__":
    main()
