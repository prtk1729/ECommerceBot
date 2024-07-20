from langchain_astradb import AstraDBVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import pandas as pd
import os
from ecombot.data_converter import data_converter

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")

embedding = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

def ingest_data(status):
    '''
    Creates a vector DB in Astra ans store all the documents there
    with the collection_name as given below
    '''
    vstore = AstraDBVectorStore(\
                                embedding = embedding,
                                collection_name="ecomChatBot",
                                api_endpoint=ASTRA_DB_API_ENDPOINT,
                                token=ASTRA_DB_APPLICATION_TOKEN,
                                namespace=ASTRA_DB_KEYSPACE
                                )

    storage = status
    if storage == None: # convert and add to vstore only once
        docs = data_converter() # list of Document() -> this format send to astra
        inserted_ids = vstore.add_documents(docs)
    else:
        return vstore
    return inserted_ids, vstore
    

if __name__ == "__main__":
    inserted_ids, vstore =ingest_data(None)
    print(f"\nInserted {len(inserted_ids)} documents.")

    # Do the similarity search on some text as Question
    results = vstore.similarity_search("Suggest a low budget sound basshead.")
    for res in results:
        print(f"* {res.page_content} [{res.metadata}]")

