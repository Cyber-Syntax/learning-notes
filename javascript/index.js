// sum function

function sum(a, b) {
    return a+b;    
}

// divide
function divide(a, b) {
    return a/b;
}

function multiply(a, b) {
    return a*b;
}

function subtract(a, b) {
    return a-b;
}

// input from console?

const string = 'string';
let boolstring=Boolean(string); // true
console.log(boolstring);

const number = -100;
let boolnumber=Boolean(number); // true
console.log(boolnumber);

// get false 
const zero = 0;
let boolzero=Boolean(zero); // false
console.log(boolzero);

const emptystring = '';
let boolemptystring=Boolean(emptystring); // false
console.log(boolemptystring);
