from retriever import create_retriever


def search_customer_query(query):
    """
    Search the company knowledge base for relevant information.

    Args:
        query (str): Customer's natural-language question.

    Returns:
        list: Relevant documents retrieved from the knowledge base.
    """
    if not query or not query.strip():
        return []

    vector_store = create_retriever()

    return vector_store.similarity_search(
        query.strip(),
        k=3
    )


if __name__ == "__main__":
    question = input("Enter customer question: ")

    results = search_customer_query(question)

    print("\n" + "=" * 60)
    print("RETRIEVED KNOWLEDGE")
    print("=" * 60)

    if not results:
        print("No relevant information found.")
    else:
        for index, document in enumerate(results, start=1):
            print(f"\nResult {index}:")
            print(document.page_content)