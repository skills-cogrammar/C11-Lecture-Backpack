let display = document.getElementById('display')

// console.log(display.value)

function appendValue(value) {
    display.value = display.value + value
} 

function clearDisplay() {
    display.value = ''
}

function calculate() {
    display.value = eval(display.value)
}