from generator import generate_flashcard

print("Testing Llama output\n")
test_input = "What is endothermic process?" 
response = generate_flashcard(test_input)

print("Response: \n" + response)
