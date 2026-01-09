

from app.services.llm_service import ask_llm


class ExplainAgent:
    def explain(
        self,
        text: str,
        mode: str = "patient",
        language: str = "english"
    ) -> str:

        # Base explanation style (MODE)
        if mode == "doctor":
            style_prompt = (
                "Explain the medical report with clinical accuracy "
                "and correct medical terminology."
            )
        else:
            style_prompt = (
                "Explain the medical report in very simple words "
                "for a normal patient. Avoid medical jargon."
            )

        # 🚀 LANGUAGE OVERRIDES MODE (VERY IMPORTANT)
        language_prompt = {
            "english": (
                "IMPORTANT: Write the ENTIRE response strictly in English only."
            ),

            "hinglish": (
                "IMPORTANT: Write the ENTIRE response strictly in Hinglish. "
                "Use Hindi sentence structure with English medical terms. "
                "DO NOT write pure English."
            ),

            "hindi": (
                "IMPORTANT: Write the ENTIRE response strictly in simple Hindi only."
            ),

            # "bhojpuri": (
            #     "IMPORTANT: Write the ENTIRE response strictly in Bhojpuri language. "
            #     "Use rural Bhojpuri. "
            #     "Medical terms may be explained in Bhojpuri style. "
            #     "DO NOT write English paragraphs."
            # ),

            "tamil": (
                "IMPORTANT: Write the ENTIRE response strictly in simple Tamil only."
            ),

            "marathi": (
                "IMPORTANT: Write the ENTIRE response strictly in simple Marathi only."
            )
        }.get(language, "Write the response in English.")

        prompt = f"""
        {style_prompt}

        {language_prompt}

        Medical Report:
        {text}
        """

        return ask_llm(prompt)
