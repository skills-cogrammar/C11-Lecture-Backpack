# Example 1: Simple if statement
age = 16
if age > 18:
    print("You are eligible to vote")
# This will not print anything because the condition is false

# Example 2: if-else statement
age = 16
if age > 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
# This will print "You are not eligible to vote"

# Example 3: if-elif-else statement
age = 16

if age < 18:
    print("You are not eligible to vote")
elif age == 18:
    print("You are now eligible to vote for the first time!")
else:
    print("You are eligible to vote")
# This will print: "You are not eligible to vote"

# Example 4: More complex conditions with and/or operators
legal_age_to_vote = 18
nationality_to_vote = "local"
henry_nationality = "local"
henry_age = 20

# Check if Henry meets both age and nationality requirements
if (henry_age >= legal_age_to_vote) and (henry_nationality == nationality_to_vote):
    print("Henry is eligible to vote")
# If Henry doesn't meet either the age or nationality requirement
elif (henry_age < legal_age_to_vote) or (henry_nationality != nationality_to_vote):
    print("Henry is not eligible to vote")
# This will print "Henry is eligible to vote"

# Example 5: with ranges
age = 20

if 0 <= age <= 12:
    print("You are a child.")
elif 13 <= age <= 19:
    print("You are a teenager.")
elif 20 <= age <= 64:
    print("You are an adult.")
else:
    print("You are a senior.")
# Output for age = 20: "You are an adult"
# Output for age = -5: "You are a senior" => In error

# Example 5: More efficient
age = 20

if 0 <= age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 64:
    print("You are an adult.")
elif age > 64:
    print("You are a senior.")
else:
    print("The age is not valid.")

# Output for age = 20: "You are an adult"
# Output for age = -5: "The age is not valid."