import kotlin.random.Random

fun main() {
    /* 
    println("Hello world!")
    val name = "Abdullah"
    val age = 15
    var num1 = 30
    var num2 : Int
    num2 = 20
    print("My name is " + name + ". ")
    println("My age is " + age + ".")
    println("Sum of 30 and 20 is " + (num1 + num2))
    */

    val maxNumber = 100
    val secretNumber = Random.nextInt(maxNumber) + 1
    var flag = true
    while (flag) {
        print("Enter guess: ")
        var ask = readLine()?.toIntOrNull() ?: -1
        if (ask == -1){
            println("Incorrect input!")
        }
        else if (ask == secretNumber){
            println("Correct guess!")
            flag = false
        }
        else {
            if (ask > secretNumber){
                println("Number greater than secret number. Try again.")
            }
            else{
                println("Number lesser than secret number. Try again.")
            }
        }


    }


}