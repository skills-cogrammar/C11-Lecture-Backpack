# Step 1 
Create an HTML file named cafe_order.html to collect user input. The HTML file should contain input fields for the following details: 

1. The user's name 
2. Their favorite type of coffee
3. Their preferred coffee size 
4. The number of cups of coffree they drink daily 
5. A number between 1 and 10 that represents their excitement level for coffee

# Step 2 
Create a JavaScript file called `cafeExperience.js` to process the user input. Using `prompt()` or by accessing the form inputs via the DOM, retrieve the following data:

- Combine the first name and coffee type ((1) and (2)) to generate their "coffee persona"
- Use (4) and (5) to calculate how many cups of coffee they would drink in the next (5) days if their exitement level remains constant.
- Use (4) and (5) to determine the average amount of time they spend in the cafe per week, assuming each cup takes 15 minutes to enjoy
- Compute (4) % (5) to determine how many "bonus" coffees they deserve in a special cafe loyalty program
- Divide (4) by (5) (rounding the result) to estimate how many people they'll convert into coffee lovers this monty

# Step 3
Display the results in a playful, multi-line message using template literals. For example:
`Welcome to the Virtual Cafe, Sarah!
Your coffee persona is: Sarah the Latte lover.
In the next 5 days, you will drink 35 cups of coffee!
This week, you'll spend 7 hours savoring coffee in the cafe.
Congratulations! You've earned 2 bonus coffees in our loyalty program.
You'll inspire 3 new coffee lovers this month - Keep spreading the love!`
