from gpt4all import GPT4All

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
model.load()

system_prompt = """
You are a flashcard generator. The user will provide a topic or question, and you will generate a concise definition or explanation. Keep your response short and factual.
"""
user_input = ""

full_prompt = system_prompt + "\nUser input" + user_input
response = model.generate(full_prompt)


flashcards = {
    "topic: ": user_input,
    "definition: ": response
}

def generate_flashcard():

    full_prompt = system_prompt + "\nUser input" + user_input
    response = model.generate(full_prompt)
    return response

