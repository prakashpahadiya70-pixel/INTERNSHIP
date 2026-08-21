from graph import build_graph


def main():

    print("=" * 65)
    print("🤖 DAY 23 - LANGGRAPH MULTI-AGENT SYSTEM")
    print("=" * 65)

    user_query = input("\nEnter your question: ")

    initial_state = {
        "user_query": user_query,
        "coordinator_result": "",
        "research_result": "",
        "final_answer": "",
        "error": ""
    }

    try:

        workflow = build_graph()

        result = workflow.invoke(initial_state)

        print("\n" + "=" * 65)
        print("FINAL RESPONSE")
        print("=" * 65)

        print(result["final_answer"])

    except Exception as e:

        print("\n❌ SYSTEM ERROR")
        print(str(e))


if __name__ == "__main__":
    main()