// This is a single-line comment
/* 
This is a
multiline
comment
*/

// Let's output a simple message
// Note single quotes aren't allowed like print('Hello, World!')
print("Hello, World!")

// Let's define some variables
var age : Int = 15
// This is also valid:
// var age = 15 (The type is inferred)
// OR
/* 
var age : Int
age = 15 (This one gives more flexibility because you can assign the value later)
*/

// Let's define some constants
let name : String = "Abdullah Abdur Rahim"
// OR
// let name = "Abdullah Abdur Rahim" (The type is inferred here)

// How to do string interpolation (commonly known as format string in Python)
var message = "Hello \(name)! Your age is \(age)."
print(message)
// OR 
// print("Hello \(name)! Your age is \(age).")

var favouriteLetter : Character

favouriteLetter = "A"
print("Your favourite letter is \(favouriteLetter)!")
// Basic data types in Swift are:
// 1. String
// 2. Character
// 3. Int
// 4. Float
// 5. Double
// 6. Bool
// 7. Dictionary
// 8. Array
// 9. Set
