from app.services.llm_service import ask_llm


class ExplainAgent:
    def explain(self, text: str, mode: str = "patient") -> str:
        """
        mode:
        - patient  -> simple explanation for normal users
        - doctor   -> clinical explanation for doctors
        - hinglish -> Hindi + English mixed explanation
        """

        if mode == "doctor":
            prompt = (
                "Explain the following medical report in clinical language "
                "using proper medical terminology for a doctor:\n\n"
                f"{text}"
            )

        elif mode == "hinglish":
            prompt = (
                "Explain the following medical report in simple Hinglish "
                "(mix of Hindi and English, easy words for Indian patients):\n\n"
                f"{text}"
            )

        else:  # patient (default)
            prompt = (
                "Explain the following medical report in very simple terms "
                "for a non-medical person. Avoid complex medical words:\n\n"
                f"{text}"
            )

        return ask_llm(prompt)
