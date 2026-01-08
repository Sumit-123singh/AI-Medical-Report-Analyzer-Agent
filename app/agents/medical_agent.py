from app.services.llm_service import ask_llm

def analyze_report(text: str) -> str:
    """
    Analyze medical report text using LLM
    """
    prompt = (
        "Analyze the following medical report and extract key findings. "
        "Do not give diagnosis:\n\n"
        f"{text}"
    )

    return ask_llm(prompt)
