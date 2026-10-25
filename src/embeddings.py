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

def create_embedding(text):
        response = client.embeddings.create(
                model="text-embedding-3-small",
                input=text
        )
        return response.data[0].embedding

#Disable Ollama
#client = OpenAI(
#    base_url="http://localhost:11434/v1",
#    api_key="ollama"
#)


#MODEL = "nomic-embed-text"


#def create_embedding(text):

#    response = client.embeddings.create(
#        model=MODEL,
#        input=text
#    )

#    return response.data[0].embedding


def embed_chunks(chunks):
    embedded_chunks = []
    for chunk in chunks:
        embedding = create_embedding(
            chunk["text"]
        )

        embedded_chunks.append({
            "text": chunk["text"],
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"],
            "embedding": embedding
        })

    return embedded_chunks

