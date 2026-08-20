from research_agent import ResearchAgent
from analyzer import Analyzer
from critic import Critic
from writer import Writer
from shared_state import SharedState


class Coordinator:

    def run(self, topic):

        print("\n[Coordinator] Starting workflow...")

        # Create shared state
        state = SharedState(topic)

        # Step 1: Research
        research_agent = ResearchAgent()
        state.research = research_agent.research(state.topic)

        print("[Research Agent] Research completed.")

        # Step 2: Analysis
        analyzer = Analyzer()
        state.analysis = analyzer.analyze(state.research)

        print("[Analyzer] Analysis completed.")

        # Step 3: Critic Review
        critic = Critic()
        state.criticism = critic.review(
            state.research,
            state.analysis
        )

        print("[Critic] Quality check completed.")

        # Step 4: Writing
        writer = Writer()
        state.final_report = writer.write(
            state.topic,
            state.research,
            state.analysis,
            state.criticism
        )

        print("[Writer] Final response generated.")

        return state.final_report