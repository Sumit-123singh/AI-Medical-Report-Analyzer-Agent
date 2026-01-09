import ollama


def ask_llm(prompt: str) -> str:
    """
    Call local Ollama LLM (llama3.2)
    No API key, no internet, completely free
    """
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful medical assistant. Explain medical reports clearly and accurately."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


