from services.llm_service import ask_llm

class ExplainAgent:
    def simplify(self, text: str, style: str = "simple") -> str:
        if style == "hinglish":
            prompt = (
                "Explain the following medical report in simple Hinglish "
                "(mix of Hindi and English, easy words):\n\n"
                f"{text}"
            )
        else:
            prompt = (
                "Explain the following medical report in very simple terms "
                "for a non-medical person:\n\n"
                f"{text}"
            )

        return ask_llm(prompt)
