from gpt4all import GPT4All

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
model.load()

system_prompt = """
You are a flashcard generator. The user will provide a question or topic in which they would like a concise and simple description or definition about the specific concept. Keep your response short. It should only be a factual description or definition. If it's related to an equation or a formula, simply provide the equation or formula. If the user provides a question, try to summarize it into one name or title. For example: "What is endomorphisis?", the topic of the card should say "Endomorphisis", and the definition should be a short description that answers the question. All definitions must be accurate
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

