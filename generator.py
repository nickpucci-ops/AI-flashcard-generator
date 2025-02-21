from gpt4all import GPT4All
import sys

model_name = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"

system_prompt = """
You are a flashcard generator. The user will provide a topic or question, and you will generate a concise definition or explanation. Keep your response short and factual.
"""
user_input = "What is a C pointer?"

flashcard = {
    "topic": user_input,
    "definition": response
}

def generate_flashcard(user_input):
    model = GPT4All(model_name, allow_download=False)
    tokens = []
    full_prompt = system_prompt + "\nUser input: " + user_input
    for token in model.generate(full_prompt, streaming=True):
        tokens.append(token)
        sys.stdout.write(token)
    sys.stdout.flush()
  
if __name__ == '__main__':
    #enter a prompt for user input 
    user_input = "What is a C pointer?"
    flashcard = generate_flashcard(user_input)

print("Flashcard: ")
print(f"Topic: {flashcard['topic']}")
print(f"Definition: {flashcard['definition']}\n")

