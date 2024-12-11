console.log("Hello, JavaScript!")

let myName = "Bonaventure"

const PI = 3.142

let isLoggedIn = false

let isAdmin = false

// let number1 = Number(prompt("Enter a number"))
// let number2 = Number(prompt("Enter another number"))


// let age = 67

// if (age >= 18 || age >=22) {
//     console.log("You are eligible to vote!")
// }

if (isLoggedIn == true && isAdmin == true) {
    console.log("Access the admin dashboard")
} else if (isLoggedIn == true && isAdmin == false) {
    console.log("Access your departmental portal.")
} else {
    console.log("You are an anonymous user!")
}


console.log(10 !== "10")