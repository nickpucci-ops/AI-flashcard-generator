from gpt4all import GPT4All

model = GPT4All("/mnt/c/Users/")
model.load()

system_prompt = """

"""
user_input = ""

full_prompt = system_prompt + "\nUser input" + user_input
response = model.generate(full_prompt)


flashcards = {
    "question: ": user_input,
    "definition: ": response
}

print(response)
