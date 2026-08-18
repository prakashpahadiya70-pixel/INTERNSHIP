import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


def web_search(query):
    try:
        if not TAVILY_API_KEY:
            return {
                "success": False,
                "error": "TAVILY_API_KEY not found in .env"
            }

        tavily = TavilyClient(api_key=TAVILY_API_KEY)

        response = tavily.search(
            query=query,
            search_depth="basic",
            max_results=5
        )

        results = []

        for result in response.get("results", []):
            results.append({
                "title": result.get("title"),
                "url": result.get("url"),
                "content": result.get("content")
            })

        return {
            "success": True,
            "query": query,
            "results": results
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


if __name__ == "__main__":

    query = input("Enter your search query: ")

    result = web_search(query)

    if result["success"]:

        print("\nWeb Search Results")
        print("=" * 60)

        for i, item in enumerate(result["results"], start=1):
            print(f"\n{i}. {item['title']}")
            print(f"URL: {item['url']}")
            print(f"Content: {item['content'][:300]}...")

    else:
        print("\nError:", result["error"])