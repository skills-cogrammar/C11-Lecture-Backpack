# Part1: Examples

# Find the last letter in a sentence. Replace every occurrence
# of this letter in the sentence with a '*'.
my_sentence = "This is my special sentence"
replace_char = my_sentence[-1]
new_char = '*'
print(replace_char)

new_sentence = my_sentence.replace(replace_char, new_char)
print(new_sentence)

# Slicing forward and backword and join
# Example: Slicing and joining a string forward and backward
example_str = "LearningPython"

# Slicing forward: First 4 characters
forward_slice = example_str[:4]  # 'Lear'

# Slicing backward: Last 4 characters in reverse
backward_slice = example_str[-4:][::-1]  # 'noht'
# or simplified
backward_slice2 = example_str[-1:-5:-1]  # 'noht'

# Joining the slices
joined_result = forward_slice + backward_slice

print("Forward slice:", forward_slice)    # Output: Lear
print("Backward slice:", backward_slice)  # Output: noht
print("Backward slice2:", backward_slice2)  # Output: noht
print("Joined result:", joined_result)    # Output: Learnoht

# Part 3: Examples
# Prompt the user to enter the student's score

score = 80

# Redundant range code.

# if score >= 90:
#     grade = "A"
# elif 90 > score >= 80:  # 90 > not required since the if eliminated all > 90
#     grade = "B"
# elif 80 > score >= 70:
#     grade = "C"
# elif 70 > score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# Determine the grade based on the score
if score >= 90:
    grade = "A"
elif score >= 80:  # 90 > not required since the if eliminated all > 90
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Display the grade
print(f"The student's grade is: {grade}")
