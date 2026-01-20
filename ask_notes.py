import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"


def load_notes():
    with open("notes.txt", "r", encoding="utf-8") as file:
        return file.read()


def ask_gemma(question, notes):
    prompt = f"""
You are a helpful assistant.
Answer the question using ONLY the notes below.

NOTES:
{notes}

QUESTION:
{question}

If the answer is not in the notes, say:
"I don't know based on the notes."
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        return "Error: Gemma not responding."

    return response.json().get("response", "")


def main():
    print("📘 Ask My Notes (Local AI)")
    print("Type 'exit' to quit\n")

    notes = load_notes()

    while True:
        question = input("You: ")

        if question.lower() == "exit":
            print("Goodbye 👋")
            break

        answer = ask_gemma(question, notes)
        print(f"\nGemma: {answer}\n")


if __name__ == "__main__":
    main()