'''
Create a program that reads a string and alternates 
between adding an @ symbol () after every other letter
for example, "hello" becomes "he@ll@o"
''' 

# h e l l o
# 0 1 2 3 4

# h e @ l l @ o

my_text = input("Enter a string: ")

new_text = ''

for text_index, text_char in enumerate(my_text):  # returns characters in string with their index
    # modulo division 9 and 3 : 9 % 3 = 0, 5 % 4 = 1
    if text_index == 0:
        new_text = new_text + text_char  # new_text += char
        # new_text = 'h' after first iteration where i = 0
    elif text_index % 2 == 0:
        new_text = new_text + '@' + text_char
    else:
        new_text = new_text + text_char

print("Modified string: ", new_text)

# --------- Demonstrating split and join methods
# split method example
sentence = "Python is fun!"
words = sentence.split(" ")  # Splits the sentence into a list of words
print(words)
# Output: ['Python', 'is', 'fun!']

# join method example
words = ['Python', 'is', 'fun!']
sentence = " ".join(words)  # Joins the words into a sentence with spaces
print(sentence)
# Output: Python is fun!
