class ResearchAgent:

    def research(self, query):

        company_knowledge = {
            "leave": "Employees can apply for leave through the HR portal.",
            "working hours": "Company working hours are Monday to Friday, 9:00 AM to 6:00 PM.",
            "salary": "Salary is processed according to the company's monthly payroll schedule.",
            "support": "Employees can contact the HR support team for assistance."
        }

        results = []

        for keyword, information in company_knowledge.items():
            if keyword in query.lower():
                results.append(information)

        if not results:
            results.append(
                "No specific company information was found for this query."
            )

        return results