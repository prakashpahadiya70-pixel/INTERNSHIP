from langchain_core.prompts import ChatPromptTemplate


# Reusable Support Prompt Template

support_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful AI Support Assistant.

Your job is to:
- Understand the user's problem.
- Give a clear and simple solution.
- Be polite and professional.
- Suggest a useful next step.

Keep your response concise and easy to understand."""
    ),
    (
        "human",
        "{user_query}"
    )
])