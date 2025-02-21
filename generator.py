from gpt4all import GPT4All
import sys

model_name = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"

system_prompt = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are a definition AI assistent for simple flashcards. Given a topic or question by the user input, you will generate a single, brief, factual definition or explanation. Your output should only be the definition, with no extra text, explanations, or clarifications. Do not write anything else. Only answer with the definition, and keep it short (2-3 sentences max).<|eot_id|><|start_header_id|>user<|end_header_id|>
User input: {input}<|eot_id|><start_header|>assistant<|end_header_id|>
"""

def generate_flashcard(user_input):
    model = GPT4All(model_name, allow_download=False)
    tokens = []
    full_prompt = system_prompt.format(input=user_input)
    output = model.generate(full_prompt, max_tokens=100).strip()
    return output
  
if __name__ == '__main__':
    user_input = input("Choose a topic: ")
    response = generate_flashcard(user_input)
    flashcard = {
        "topic": user_input,
        "definition": response
    }

print("\n\nFlashcard ")
print(f"Topic: {flashcard['topic']}")
print(f"Definition: {flashcard['definition']}\n")

