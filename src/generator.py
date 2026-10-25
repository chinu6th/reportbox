from openai import OpenAI
from dotenv import load_dotenv
import os

# loading environment into python program
load_dotenv()

# Create the client here
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("api_key")
)

#MODEL = "qwen3:1.7b"
MODEL="gpt-4.1-mini"

def generate_answer(
    query,
    results
):

    context = "\n\n".join(
        result["text"]
        for result in results
    )

    prompt = f"""
Answer the user's question using
only the provided context. Please provide only the SQL statement nothing else as answer.
remove the top ```sql and bottom ``` . 
Answer should be only select statement . Example : Select * from table_name which can be executable in Postgrace ;

Context:
{context}

Question:
{query}

Rules:

1. Use only the provided context.
2. Do not invent information.
3. If the answer is not present,
   say that the information is
   not available.
4. Give a clear and concise answer.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return (
        response
        .choices[0]
        .message
        .content
        .strip()
    )

