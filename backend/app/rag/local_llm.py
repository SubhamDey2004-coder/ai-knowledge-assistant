import ollama

def generate_answer_stream(question, context):

    prompt = f"""
You are a document assistant.

Answer the question ONLY using the information in the context.

Rules:
- Give a short factual answer.
- Do not explain.
- Do not summarize.
- If the answer exists in the context, extract it exactly.
- If the answer is not in the context, say: "I could not find the answer in the documents."

Context:
{context}

Question:
{question}

Answer:
"""

    stream = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    for chunk in stream:
        yield chunk["message"]["content"]