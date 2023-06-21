# Queue

A queue is a linear data structure that follows the principle of "first-in, first-out" (FIFO).It represents a collection of elements where new elements are inserted at one end(back), and existing elements are removed from the other end (front).

The purpose of using queue is to provide an efficient way to manage elements in a sequential order, following the FIFO principle. It allows for the insertion of elements at one end and removal from the other, making it suitable for scenarios where order matters, such as task scheduling, event handling, and managing resources in a fair manner.

## EXAMPLE OF QUEUE

A queue can be visualized as a real-life queue, such as people waiting in line.

![guess_design](queue.jpeg)

The person who arrives first joins the queue first and gets served first, while the person who arrives later joins at the end and gets served after everyone ahead of them.

When the person at the front is removed from the queue we call this a dequeue operation. When a new person joins the queue at the back, we call this an enqueue operation. No one can cheat and enter the line in the middle of the queue.

## QUEUES IN PYTHON

Sometimes we want to repeat something a certain number of times.  In this case, we don't have a collection  to loop through.  In Python, we can use the `range` function to create a "list" of numbers.  The `range` does not really give you a list, but its like a list in that you can loop through it with a `for` loop.  This can be very useful if we want to build a loop to repeat something.  For example, if we wanted to print out "Hello" 100 times, we could write the following:

```python
for x in range(100):
    print("Hello")
```

In this code, the `range(100)` will create a list of numbers from 0 to 99.  If we loop through that list, it will run 100 times.  The result is "Hello" printed 100 times.  Notice that the variable `x` is not being used in the loop block.  This is common when all we wanted to do was to repeat the code in the block.

## While Loops

The `while` loop also repeats a block of code but the number of times the loop will run is usually not known.  The `while` loop includes a boolean condition to determine if the loop should continue running.

```python
choice = None
while choice != "quit":
    choice = input("Enter a command: ")
    
    # Do something based on the value of choice
```

Notice that this loop will continue to run so long as the user does not type "quit" for the command.  This loop might run only 1 time if the user types "quit" for their first command or the loop might run forever if the user never types "quit".  It's also possible for a while loop to not run at all.  Imagine if choice was already equal to "quit" before we got to the while loop.  If this was the case, then we would not enter the while loop.  It's important to think about how we will allow entry to the `while` loop.  In this case, we choose to set `choice` equal to `None` (which is a safe value).  Since `None` does not equal "quit", we know that we will run the while loop at least one time. 

## Example: Random Number Guessing Game

When we design loops, it can be useful to draw a flow chart of how we want our program to run.  Designing software before writing code is a wise first step.  A flow chart is a simple design technique where rectangle boxes are used to represents actions and diamonds are used to represent decisions.  Arrows are drawn to represent the flow between boxes and diamonds.  The following flow chart represents a random number guessing game. 

![guess_design](queue.jpeg)

In the flow chart, notice that the arrows are forming cycles or loops.  This is an indication that loops should be added to your code.  The design may lead you to write the code a very specific way.  Its also possible that you can simplify your code by reconsidering and redrawing your flow chart.  For the chart above, we have a `while` loop within a `while` loop.  The outer `while` loop (the red line in the flow chart) is used to allow the user to play a new game again.  The inner `while` loop (the blue line in the flow chart) is used to allow the user to continue guessing the number until they get it right.  The boolean conditions for those while loops can be determined by looking at the chart.  The red loop continues so long as the user says "YES" to the play again prompt.  The blue loop continues so long as the guess does not match.  Compare the code below with the design above.

```python
import random

print("Welcome")
play_again = "YES"  # This will allow us into the loop the first time
while play_again == "YES":
    rand_num = random.randint(1,100)
    num_guesses = 0
    guess = -1 # This will allow us into the loop the first time
    while guess != rand_num:
        guess = int(input("Enter a guess: "))
        num_guesses += 1
        if guess < rand_num:
            print("Higher!")
        elif guess > rand_num:
            print("Lower!")
    print("Congrats!")
    print("It took {} guesses.".format(num_guesses))
    play_again = input("Play again? ")
print("Goodbye")
```

## Problem to Solve : Geometric Series Sum

Write a program that will allow the user to estimate the sum of geometric series.  A geometric series one where each element in the series is calculated by multiplying the previous value by a constant.  For example, here is a geometric series:
$$
1, \frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{16}, \frac{1}{32}
$$
The series begins at 1 (called the initial term) and each number is determined by multiplying the previous number by 0.5 (called the series).  You should use a loop to add all of the numbers in the series.  You will have to ask the user for three things:

- What is the initial term in the series
- What is the ratio to use to calculate each number in the series
- How many terms in the series to calculate and add together (not including the initial term)

After displaying the answer, you should allow the user to calculate another sum instead of exiting the program.  You can ignore cases where the user types in invalid values (e.g. ratio of 0, number of terms in the series <= 0, etc).

The example execution show how a ratio of 0.5 converges the sum towards 2 and how a ratio of 2 does not converge but instead goes towards infinity.

```
Initial Term: 1
Ratio: 0.5
Terms to add: 5
Sum = 1.96875000000000000000

Again (Y/N)? Y
Initial Term: 1
Ratio: 0.5
Terms to add: 20
Sum = 1.99999904632568359375

Again (Y/N)? Y
Initial Term: 1
Ratio: 0.5
Terms to add: 50
Sum = 1.99999999999999911182

Again (Y/N)? Y
Initial Term: 1
Ratio: 2
Terms to add: 5
Sum = 63.00000000000000000000

Again (Y/N)? Y
Initial Term: 1
Ratio: 2
Terms to add: 20
Sum = 2097151.00000000000000000000

Again (Y/N)? Y
Initial Term: 1
Ratio: 2
Terms to add: 50
Sum = 2251799813685247.00000000000000000000

Again (Y/N)? N
```

You can check your code with the solution here: [Solution](geometric_series_sum.py)



[Back to Welcome Page](0-welcome.md)



