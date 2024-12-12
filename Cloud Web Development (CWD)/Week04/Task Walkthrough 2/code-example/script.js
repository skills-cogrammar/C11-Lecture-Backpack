// console.log("Please, smile!")

// let name = prompt("What's your name? ");

// let favoriteAnimal = prompt("What is your favourite animal? ");

// let favouriteHobby = prompt("What is your favourite Hobby? ");

// let age = prompt("How old are you? (Please enter a number) ");


// // generate compliment

// const compliment = `Hi ${name}! You must be good at ${favouriteHobby}. At ${age} years old, you have good energy and a spirit of a ${favoriteAnimal}`;

// alert(compliment);

// console.log(compliment)


let totalBill = parseFloat(prompt("What is the total bill? "))

let numberOfPeople = parseInt(prompt("How many people are splitting the bill? "))

let tipPercentage = parseFloat(prompt("Tip percentage? "))


let tipAmount = totalBill * tipPercentage/100

alert(`Tip amount is ${tipAmount}`)