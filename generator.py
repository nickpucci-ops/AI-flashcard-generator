from gpt4all import GPT4All
import sys

model_name = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"

system_prompt = """
Given a topic or question, you will generate a **single, brief, factual definition or explanation**. Your output should **only be the definition**, with no extra text, explanations, or clarifications. Do not write anything else. Only answer with the definition, and keep it short (2-3 sentences max). Here is the topic: 
"""

def generate_flashcard(user_input):
    model = GPT4All(model_name, allow_download=False)
    tokens = []
    full_prompt = system_prompt + user_input
    output = model.generate(full_prompt, max_tokens=90).strip()
    #for token in model.generate(full_prompt, max_tokens=50):
    #    tokens.append(token)
    #    sys.stdout.write(token)
    #sys.stdout.flush()
    #response = ' '.join(word.strip() for word in tokens if word.strip())
    #return response.strip(' ')
    return output
  
if __name__ == '__main__':
    #enter a prompt for user input 
    user_input = "What is a quantum computer?"
    response = generate_flashcard(user_input)
    flashcard = {
        "topic": user_input,
        "definition": response
    }

print("\n\nFlashcard ")
print(f"Topic: {flashcard['topic']}")
print(f"Definition: {flashcard['definition']}\n")

