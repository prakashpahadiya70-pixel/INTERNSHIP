from retriever import retrieve_relevant_documents
from response_generator import generate_response


def run_customer_support():
    """Run the RAG-based customer support feature."""
    print("=" * 60)
    print("          AI CUSTOMER SUPPORT AGENT")
    print("=" * 60)

    customer_query = input("\nCustomer Question: ").strip()

    if not customer_query:
        print("\nPlease enter a valid customer question.")
        return

    try:
        retrieved_documents = retrieve_relevant_documents(
            customer_query,
            k=3
        )

        response = generate_response(
            customer_query,
            retrieved_documents
        )

        print("\n" + "=" * 60)
        print("CUSTOMER SUPPORT RESPONSE")
        print("=" * 60)
        print(response)

    except Exception as error:
        print("\nUnable to process the request.")
        print(f"Error: {error}")


if __name__ == "__main__":
    run_customer_support()