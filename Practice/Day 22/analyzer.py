class Analyzer:

    def analyze(self, research):

        if not research:
            return ["No information available for analysis."]

        analysis = []

        for information in research:
            analysis.append(
                f"Relevant support information identified: {information}"
            )

        analysis.append(
            "The information is relevant to the user's support query."
        )

        return analysis