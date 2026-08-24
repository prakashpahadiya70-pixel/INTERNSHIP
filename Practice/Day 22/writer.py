class Writer:

    def write(self, query, research, analysis, criticism):

        if not research:
            return (
                "I'm sorry, but I could not find relevant "
                "company information for your query."
            )

        answer = research[0]

        return f"""
==============================
      AI CUSTOMER SUPPORT
==============================

Customer Query:
{query}

Response:
{answer}

Additional Information:
Please contact the company support team if you
need further assistance.

Quality Status:
Reviewed by the Critic Agent.
"""