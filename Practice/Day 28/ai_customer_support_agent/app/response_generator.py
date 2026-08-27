import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# Load environment variables from the project-level .env file.
ENV_FILE = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_FILE)


def get_llm():
    """Create and return the Gemini language model."""
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("GOOGLE_API_KEY is not configured.")

    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        google_api_key=api_key
    )


def generate_response(customer_query, retrieved_documents):
    """
    Generate a grounded customer support response.

    Args:
        customer_query (str): Customer's question.
        retrieved_documents (list): Relevant knowledge-base documents.

    Returns:
        str: AI-generated customer support response.
    """
    if not customer_query or not customer_query.strip():
        return "Please enter a valid customer question."

    if not retrieved_documents:
        return (
            "I could not find reliable information in the company "
            "knowledge base. Please contact human customer support."
        )

    context = "\n\n".join(
        document.page_content
        for document in retrieved_documents
    )

    prompt = f"""
You are a customer support assistant for TechNova Solutions.

Answer the customer's question using ONLY the information
provided in the company knowledge base below.

Do not use outside knowledge.
Do not invent or assume information.
If the knowledge base does not contain enough information,
say that reliable information is unavailable and recommend
contacting human customer support.

Company Knowledge Base:
{context}

Customer Question:
{customer_query}

Provide a concise and helpful answer.
"""

    llm = get_llm()
    result = llm.invoke(prompt)

    # Handle structured Gemini content and return plain text.
    if isinstance(result.content, list):
        return "\n".join(
            item.get("text", "")
            for item in result.content
            if isinstance(item, dict) and item.get("type") == "text"
        ).strip()

    return str(result.content)