from gpt4all import GPT4All
import sys

model_name = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"

system_prompt = """
You are a flashcard generator. Given a topic or question, you will generate a concise definition or explanation. Keep your response short and factual. Do not output anything except for the the definition to the following topic: 
"""

def generate_flashcard(user_input):
    model = GPT4All(model_name, allow_download=False)
    tokens = []
    full_prompt = system_prompt + user_input
    for token in model.generate(full_prompt, max_tokens=50, streaming=True):
        tokens.append(token)
        sys.stdout.write(token)
    sys.stdout.flush()
    return tokens
  
if __name__ == '__main__':
    #enter a prompt for user input 
    user_input = "What is a C pointer?"
    response = generate_flashcard(user_input)
    flashcard = {
        "topic": user_input,
        "definition": response
    }

print("Flashcard: ")
print(f"Topic: {flashcard['topic']}")
print(f"Definition: {flashcard['definition']}\n")

