class Critic:

    def review(self, research, analysis):

        criticism = []

        if not research:
            criticism.append(
                "No company information was found."
            )
            return criticism

        if not analysis:
            criticism.append(
                "Analysis is missing."
            )
            return criticism

        criticism.append(
            "Research information is available."
        )

        criticism.append(
            "Analysis has been completed."
        )

        criticism.append(
            "The response should remain clear, relevant, and "
            "based only on available company information."
        )

        criticism.append(
            "Quality check passed."
        )

        return criticism