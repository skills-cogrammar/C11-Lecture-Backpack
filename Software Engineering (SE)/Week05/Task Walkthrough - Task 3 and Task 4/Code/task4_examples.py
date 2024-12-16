# Part1: Examples

# Example: Receive words in a loop and concatenate them into a sentence
print("Enter words to form a sentence. Type 'stop' to finish.")

sentence = ""  # Initialise an empty string for the sentence
word = ""  # Variable to hold the current input

while word.lower() != "stop":  # Continue until 'stop' is entered
    word = input("Enter a word (or 'stop' to finish): ")
    if word.lower() != "stop":  # Avoid adding 'stop' to the sentence
        sentence += word + " "  # Concatenate the word with a space

# Remove trailing space and display the sentence
final_sentence = sentence.strip()
print("Your sentence is:", final_sentence)
