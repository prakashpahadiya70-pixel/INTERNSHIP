from coordinator import Coordinator


def main():

    print("=" * 50)
    print("🤖 MULTI-AGENT RESEARCH ASSISTANT")
    print("=" * 50)

    topic = input("\nEnter your research topic: ")

    coordinator = Coordinator()

    result = coordinator.run(topic)

    print("\n" + "=" * 50)
    print("FINAL RESEARCH REPORT")
    print("=" * 50)

    print(result)


if __name__ == "__main__":
    main()