from llama_index import VectorStoreIndex
from llama_index.readers import SimpleWebPageReader


def main(urls: list[str]) -> None:
    documents = SimpleWebPageReader(html_to_text=True).load_data(urls=urls)
    index = VectorStoreIndex.from_documents(documents=documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("What is LlamaIndex?")
    print(response)


if __name__ == "__main__":
    main(
        urls=[
            "https://nanonets.com/blog/llamaindex/",
        ]
    )
