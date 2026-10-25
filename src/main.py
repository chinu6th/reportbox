from pathlib import Path
from advanced_rag import (build_rag,retrieve)
from generator import ( generate_answer)
from report_builder import generate_report
from dotenv import load_dotenv
import os
from sql_result import run_sql_from_generator


# loading environment into python program
load_dotenv()

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

        final_Query = generate_report(query, results)
        ROWS = run_sql_from_generator(query, results)
        

        print("\nRAG :")

        print(final_Query)
        #print(final_answer)
        print("Database Results:")
        for row in ROWS:
            print(ROWS)

if __name__ == "__main__":
    main()
