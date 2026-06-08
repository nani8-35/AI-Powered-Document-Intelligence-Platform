import time
from ollama import chat

def ask_llm(context, question):
    start = time.time()

    prompt = f"""
    Context:
    {context}

    Question:
    {question}

    Answer only using the provided context.
    """

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(
        f"LLM Response Time: {time.time() - start:.2f} seconds"
    )

    return response["message"]["content"]