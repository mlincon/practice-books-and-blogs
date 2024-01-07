import os

import pinecone
from dotenv import load_dotenv
from llama_index import SimpleDirectoryReader as SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding as OpenAIEmbedding
from llama_index.llms import OpenAI as OpenAI

# from llama_index import download_loader, ServiceContext, VectorStoreIndex, StorageContext
from llama_index.vector_stores import PineconeVectorStore as PineconeVectorStore

load_dotenv()

pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],
    environment=os.environ["PINECONE_ENVIRONMENT"],
)


def main():
    pass


if __name__ == "__main__":
    main()
