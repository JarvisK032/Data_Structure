# Set

A set is a data structure that represents a collection of distinct elements with no specific order. The purpose of using sets are to ensure uniqueness, perform efficient membership testing, and leverage set operations for combining, comparing, or analyzing collections of elements. Sets provide a convenient and efficient way to work with distinct values and solve problems related to uniqueness and set theory. It is commonly used to perform operations such as membership testing, intersection, union, and difference.

## EXAMPLE OF SET

Let's use hashing as an example, the set is able to add, remove, and test for membership in O(1) time.

![guess_design](queue.jpeg)

The person who arrives first joins the queue first and gets served first, while the person who arrives later joins at the end and gets served after everyone ahead of them.

When the person at the front is removed from the queue we call this a dequeue operation. When a new person joins the queue at the back, we call this an enqueue operation. No one can cheat and enter the line in the middle of the queue.

## SET IN PYTHON

In Python, a set can be represented using a curly braces (e.g. my_set = {1, 2, 3}) To create an empty set (unlike an empty list), we use the code: empty_set = set().

Here's an example of how to use a set in Python:

```python
# Creating a set
fruits = {'apple', 'banana', 'orange', 'apple', 'pear'}

print(fruits)
# Expected Result: {'apple', 'pear', 'banana', 'orange'}

# Adding elements to a set
fruits.add('grape')
print(fruits)
# Expected Result: {'apple', 'pear', 'banana', 'grape', 'orange'}

# Removing an element from a set
fruits.remove('banana')
print(fruits)
# Expected Result: {'apple', 'pear', 'grape', 'orange'}

# Checking membership in a set
print('apple' in fruits)
# Expected Result: True

# Performing set operations
vegetables = {'carrot', 'spinach', 'tomato', 'apple'}

# Union of two sets
all_items = fruits.union(vegetables)
print(all_items)
# Expected Result: {'apple', 'carrot', 'spinach', 'grape', 'tomato', 'orange', 'pear'}

# Intersection of two sets
common_items = fruits.intersection(vegetables)
print(common_items)
# Expected Result: {'apple'}

# Difference between two sets
unique_fruits = fruits.difference(vegetables)
print(unique_fruits)
# Expected Result: {'pear', 'grape', 'orange'}

# Size of a set
print(len(fruits))
# Expected Result: 4


```

In the above example, a set called fruits is created, containing various fruit names. Since sets do not allow duplicates, any duplicate elements are automatically removed. Elements can be added to the set using the add() method and removed using the remove() method.

Membership testing is demonstrated by checking if the element 'apple' is present in the set. Set operations like union, intersection, and difference are performed between the fruits set and a vegetables set. The size of the set is obtained using the len() function.

The performance of the set is based on the performance of the hashing algorithm.

![guess_design](set2.png)



## Example Code: Print Job Scheduler

In this scenario, you are developing a print job scheduler for a printer. Multiple users send print jobs to the printer, and the scheduler needs to ensure that the jobs are processed in the order they were received.

```python
class PrintJobScheduler:
    def __init__(self):
        self.queue = []

    def enqueue_job(self, job):
        self.queue.append(job)
        print(f"Job '{job}' added to the print queue.")

    def process_jobs(self):
        while self.queue:
            job = self.queue.pop(0)
            print(f"Printing job: '{job}'")

scheduler = PrintJobScheduler()

# Enqueue print jobs
scheduler.enqueue_job("Document1")
scheduler.enqueue_job("Document2")
scheduler.enqueue_job("Document3")

# Process print jobs
scheduler.process_jobs()

```
Using a queue in this scenario ensures that the print jobs are processed in the order they were received, following the FIFO principle. It provides a fair scheduling mechanism where the first job to arrive is the first to be printed.

The queue allows for efficient insertion of new print jobs at the back and removal of jobs from the front, ensuring that the jobs are processed in the correct order. It also handles cases when multiple print jobs are submitted concurrently, managing them in a sequential manner.

## Problem to Solve : Call Center Customer Support

Write a program to help the call center receives incoming customer calls that need to be handled by customer support representatives. The calls should be serviced in the order they are received.


You can check your code with the solution here: [Solution](callcenter.py)



[Back to Welcome Page](0-Welcome.md)



