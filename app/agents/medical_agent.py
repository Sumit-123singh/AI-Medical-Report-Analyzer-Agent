from services.llm_service import ask_llm


class MedicalAgent:
    def analyze_report(self, report_text: str) -> str:
        """
        Analyze medical report and extract clinical meaning
        """
        prompt = f"""
        You are a medical expert.
        Analyze the following medical report and explain:
        - Key findings
        - Abnormal values
        - Possible conditions

        Medical Report:
        {report_text}
        """

        response = ask_llm(prompt)
        return response
