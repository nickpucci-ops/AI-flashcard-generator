from gpt4all import GPT4All

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
model.load()

system_prompt = """
You are a flashcard generator. The user will provide a question or topic in which they would like a concise and simple description or definition about the specific concept. Keep your response short. It should only be a factual description or definition. If it's related to an equation or a formula, simply provide the equation or formula. All definitions must be accurate
"""
user_input = ""

full_prompt = system_prompt + "\nUser input" + user_input
response = model.generate(full_prompt)


flashcards = {
    "question: ": user_input,
    "definition: ": response
}

