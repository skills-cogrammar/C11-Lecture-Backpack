let input = prompt("Write a word you want to reverse: ");

// Using two strings
let counter = input.length - 1;
let reveresedInput = "";

while (counter >= 0){
    reveresedInput = reveresedInput + input[counter];
    counter = counter - 1;
}

console.log(reveresedInput)

// Using an array and two pointer approach (Array is more efficient than
// a string for performing transformations of the values)
input = input.split("");

let leftPointer = 0; // first index of the word
let rightPointer = input.length - 1; // Get the last index of the input

while (leftPointer < rightPointer) {
    const temp = input[leftPointer] // get the old value so that it can be used again after the value at the index changes
    input[leftPointer] = input[rightPointer];
    input[rightPointer] = temp

    leftPointer = leftPointer + 1; // leftPointer++;
    rightPointer = rightPointer - 1; // rightPointer--;
}

input = input.join("") // Turn the array into a string
console.log(input)