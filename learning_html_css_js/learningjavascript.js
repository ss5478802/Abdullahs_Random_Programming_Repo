// Learning JavaScript from "Javascript All-In-One book For Dummies" book (btw this is a single-line comment)

/*
This a multi-line
comment. 
*/

let randomString = "duofhWrgSyT"; // A string
let listOfVowels = "a,e,i,o,u";
let message = "Learn Java!"; // Another string
const constantNumber = 9;
let changingNumber = 2;
console.log(randomString.charAt(4)); // Prints the letter at the given index in the string
console.log(randomString.indexOf("g")); // Prints the index of the first occurence of the letter
console.log(randomString.length); // Prints the length of the string
console.log(randomString.toUpperCase()); // Converts the whole string to upper case temporarily
console.log(randomString.toLowerCase()); // Converts the whole string to lower case temporarily
console.log(
  randomString.slice(3, 8)
); /* Returns the letter for the first number metioned upto 
      but not to the second number 
      (note: randomString.slice(8,3) will return empty string) */
console.log(randomString.substring(3, 8)); // Return the letters from the lowest value to the highest value.
console.log(message); // Printing a string
message = message.replace("Java", "Python"); // Replacing a group of letter with a new set of letter
console.log(message);
console.log(constantNumber);
// "constantNumber = 6;" wil give an error since constant value can't be changed
console.log(`Value of changingNumber variable: ${changingNumber}`);
changingNumber = 12;
console.log(`Value of changingNumber variable: ${changingNumber}`);
// listOfVowels = listOfVowels.split(",");
console.log(listOfVowels.split(","));
console.log(listOfVowels);
