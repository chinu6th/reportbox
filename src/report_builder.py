from sql_result import run_sql_from_generator
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(base_url=os.getenv("BASE_URL"),
                api_key=os.getenv("api_key"))
MODEL = "gpt-4.1-mini"

row = run_sql_from_generator(query,results)

def generate_report(row):
    context = "\n".join(str(row) for row in rows)

    prompt = f"""
You are a Report Builder tool. Based on the following database query results,
Prepare a clear and concise report with multi dimensional features.

Query: {query}
Results:
{context}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()