const name = prompt("Enter you name: ");
const favCoffee = prompt("Enter your fav coffee: ");
const prefSize = prompt("What is your prefered coffee size: ");
const cupsPerDay = Number(prompt("How many cups of coffee do you have per day: "));
const coffeeRating = Number(prompt("What is your excitement level towards coffee, give a rating between 1 and 10: "));

// Concat
// const coffeePersona = name + " " + favCoffee;

// List Approach
// const coffeePersona = [name, favCoffee].join(" ")

// Template Literal 
const coffeePersona = `${name} ${favCoffee}`
const coffeesInFiveDays = cupsPerDay * 5;
const totalCoffeeTimePerWeek = (cupsPerDay * 15) * 5;
const bonusCoffees = cupsPerDay % coffeeRating;
const peopleConverted = cupsPerDay / coffeeRating;

const finalReport = `Welcome to the Virtual Cafe, ${name}!
Your coffee persona is: ${coffeePersona}.
In the next 5 days, you will drink ${coffeesInFiveDays} cups of coffee!
This week, you'll spend ${totalCoffeeTimePerWeek / 60} hours savoring coffee in the cafe.
Congratulations! You've earned ${bonusCoffees} bonus coffees in our loyalty program.
You'll inspire ${Math.round(peopleConverted)} new coffee lovers this month - Keep spreading the love!`

console.log(finalReport)