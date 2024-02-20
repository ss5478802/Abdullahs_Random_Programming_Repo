"""
no_of_people = int(input("How many people are there? "))

list_of_name = [None] * no_of_people
index = 0

while True:
    if index == no_of_people:
        print(list_of_name)
        break
    else:
        name = input("Enter the person's name: ")
        if name == "":
            name = input("Enter the person's name: ")
        else:
            list_of_name[index] = name
            index += 1


searchname = input("Enter name to search: ")

found = False
place = 1

for i in range(0, len(list_of_name) - 1):
    if list_of_name[i] == searchname:
        found = True
        place = i

if found == True:
    print(searchname, "was found at postion", place + 1, "in the list!")
else:
    print(searchname, "was not found in the list!")
"""

"""
from time import *
# Least efficient bubble sort algorithm (algorithm written by me, not copied from google!)
mylist = [31, 32, 35, 36, 37, 38, 39, 42]

starttime = time()
for round in range(0, len(mylist)):
    for counter in range(0, len(mylist) - 1):
        if mylist[counter] > mylist[counter + 1]:
            temp = mylist[counter]
            mylist[counter] = mylist[counter + 1]
            mylist[counter + 1] = temp
        print(mylist)

print("This took", (time()-starttime), "seconds.")

# Most efficient bubble sort algorithm (algorithm written by me, not copied from google!)
mylist2 = [31, 32, 35, 36, 37, 38, 39, 42]

last = len(mylist2)

starttime2 = time()

while True:
    correct = 0
    for i in range(0, last - 1):
        if mylist2[i] > mylist2[i + 1]:
            temp2 = mylist2[i]
            mylist2[i] = mylist2[i + 1]
            mylist2[i + 1] = temp2
            
        else:
            correct += 1
        print(mylist2)

    last -= 1
    if correct == (len(mylist2) - 1):
        break

print("This took", (time()-starttime2), "seconds.")
"""
'''
print("""Enter your choice:
A for Add
S for Subtract """)
'''
"""
print("How many tickets do you want to buy?")

while True:
    ticket = int(input())
    if ticket > 25 or ticket <= 0:
        print("1-25 tickets can be bought in a single transaction.")
        print("Enter again!")
    else:
        break

discount = 0
if ticket < 10:
    discount = 0
elif ticket >= 10 and ticket < 20:
    discount = 0.1
else:
    discount = 0.2

total = (1 - discount) * (20 * ticket)
print("Your total cost is $" + str(total) + "0")
"""
"""
x = int(input("Enter the number for factorial: "))
fact = 1
for i in range(1, x+1):
    fact = fact * i
print(fact)
"""
"""
temp = [0,1,2,3,4,5,6]
for i in range(0, 7):
    print(temp[i], end=" ")
"""

"""
x = 1
num = int(input("Enter number: "))
def fact(numw):
    global x
    x = x * numw
    numw -= 1
    if numw != 1:
        fact(numw)
    return x

print(fact(num))
"""
"""
y = 1
def output():
    global y 
    y = y + 1
    return y

print(output())
"""

# file = open(r"C:\Users\Acer\Desktop\olevel.txt", "w")
# file.writelines("Hello! I'm Abdullah!")
# file.close()
# file = open(r"C:\Users\Acer\Desktop\olevel.txt", "r")
# print(file.read())
# file.close()
"""
import random as rm
from emoji import emojize

choice_list = [
    f"rock {emojize(':raised_fist:')}",
    f"paper {emojize(':raised_hand:')}",
    f"scissor {emojize(':victory_hand:')}",
]
c_choice = rm.choice(choice_list)
h_choice = input("Enter rock, paper or scissor: ")

if h_choice == "rock":
    print(f"You chose {choice_list[0]} and I chose {c_choice}. So the result is:")
elif h_choice == "paper":
    print(f"You chose {choice_list[1]} and I chose {c_choice}. So the result is:")
else:
    print(f"You chose {choice_list[2]} and I chose {c_choice}. So the result is:")


if c_choice == h_choice:
    print("Tie!")
elif c_choice == "rock" and h_choice == "paper":
    print("You win!")
elif c_choice == "rock" and h_choice == "scissor":
    print("I win!")
elif c_choice == "paper" and h_choice == "rock":
    print("I win!")
elif c_choice == "paper" and h_choice == "scissor":
    print("You win!")
elif c_choice == "scissor" and h_choice == "rock":
    print("You win!")
else:
    print("I win!")
"""
"""
text = input("Enter text to translate: ")
text = (
    text.replace("a", "4")
    .replace("b", "8")
    .replace("e", "3")
    .replace("l", "1")
    .replace("o", "0")
    .replace("s", "5")
    .replace("t", "7")
)
print(text)
"""
"""
# Sample use of map()
x = ["ad","bd","aaab","baa","badab"]
x = list(map(lambda a: a.upper(), x))
print(x)
"""
"""
# Sample use of reduce()
from functools import reduce

cart = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = reduce(lambda x, y: x + y, cart)
print(total)
"""
"""
# Sample use of filter()
list_of_numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
]
odd_numbers = list(filter(lambda x: x % 2 != 0, list_of_numbers))
print(odd_numbers)
"""
"""
# Use of enumerate()
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
while True:
    try:
        print(next(y))
    except StopIteration:
        print()
        print("Manual \"FOR\" loop done! \n")
        break
for i, j in enumerate(x):
    print(f"{i+1}.", j)
z = enumerate(range(0, 11))
print(list(z))
"""
"""
# Fibonacci sequence using generators(the function is the generator)
def fibo():
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first+second

fibo = fibo()
for _ in range(0, 20):
    print(next(fibo), end = " ")
"""
"""
# Generating square numbers using generator
print("10 square numbers:")
x = (i**2 for i in range(0, 11))
while True:
    try:
        print(next(x), end = " ")
    except StopIteration:
        break
"""

"""
# bubble sort algorithm
def bubble(f):
    for i in range(0, len(f)):
             swap = False
             for i in range(0, len(f)-1-i):
                     if f[i] > f[i+1]:
                             temp = f[i]
                             f[i] = f[i+1]
                             f[i+1] = temp
                             swap = True
             if swap != True:
                     return f
                     break

"""
"""
# Selection sort algorithm
def selection(f):
    for i in range(0, len(f)-1):
            small = i
            for j in range(i+1, len(f)):
                    if f[j] < f[small]:
                            small = j
            f[small], f[i] = f[i], f[small]
    return f

"""
"""
# Insertion sort algorithm
def insertion(f):
    for i in range(1, len(f)):
            current = f[i]
            j = i-1
            while j >= 0 and f[j] > current:
                    f[j+1] = f[j]
                    j -= 1
            f[j+1] = current
    return f

"""
"""
# Merge sort algorithm
def merge_sort(x):
    if len(x) <= 1:
        return x
    else:
        mid = len(x) // 2
        left = x[:mid]
        right = x[mid:]
        leftsort = merge_sort(left)
        rightsort = merge_sort(right)
        ans = []
        while leftsort and rightsort:
            if leftsort[0] < rightsort[0]:
                ans.append(leftsort.pop(0))
            else:
                ans.append(rightsort.pop(0))
        ans.extend(leftsort or rightsort)
    return ans
        
x = [100,87,5,3,-1,55,42,-99,-342,343,1000,-543,24,1,34,6,4,2,1,3045,-4534,20,-453]
print(merge_sort(x))
"""
"""
# Quicksort algorithm
def quicksort(x):
    if len(x) <= 1:
        return x
    else:
        low = x[0]
        mid = x[len(x) // 2]
        high = x[len(x)-1]
        pivot = 0
        # Find pivot using median
        if low <= mid <= high:
            pivot = mid
        elif low <= high <= mid:
            pivot = high
        elif high <= low <= mid:
            pivot = low
        elif high <= mid <= low:
            pivot = mid
        else:
            pivot = low
        x.remove(pivot)
        left = []
        right = []
        for i in x:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        return quicksort(left) + [pivot] + quicksort(right)

x = [100,87,5,3,-1,55,42,-99,-342,343,1000,-543,24,1,34,6,4,2,1,3045,-4534,20,-453]
print(quicksort(x))
"""
"""
# For binary search algorithm, array should be sorted
def binarysearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return f"Found At Index: {mid + 1}"
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return "Not found!" 
x = [100,87,5,3,-1,55,42,-99,-342,343,1000,-543,24,1,34,6,4,2,1,3045,-4534,20,-453]
x = list(set(x))
x.sort()
print(binarysearch(x, 20))
"""


class NodeForSinglyLinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


n3 = NodeForSinglyLinkedList(2)
n2 = NodeForSinglyLinkedList(3)
n1 = NodeForSinglyLinkedList(-1)
n4 = NodeForSinglyLinkedList(0)
n5 = NodeForSinglyLinkedList(100)
n6 = NodeForSinglyLinkedList(-7)
n7 = NodeForSinglyLinkedList(50)


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def printlist(self):
        current = self.head
        list_to_print = []
        while current:
            list_to_print.append(current.value)
            current = current.next
        print(list_to_print)

    def delete_node(self, node):
        current = self.head
        prev = None
        if current.value == node.value:
            self.head = current.next
        else:
            while current:
                if current.value == node.value:
                    break
                else:
                    prev = current
                    current = current.next
            if current != None:
                prev.next = current.next
                current = None

    def insert_node(self, new_node, position=None):
        current = self.head
        count = 1
        if position == 1:
            new_node.next = self.head
            self.head = new_node
        elif position == None:
            self.append(new_node)
        else:
            while current:
                if count + 1 == position:
                    new_node.next = current.next
                    current.next = new_node
                    break
                else:
                    count += 1
                    current = current.next


l = SinglyLinkedList(n1)
l.append(n2)
l.append(n3)
l.append(n4)
l.append(n5)
l.append(n6)
l.append(n7)
l.printlist()
l.delete_node(n5)
l.printlist()
l.insert_node(NodeForSinglyLinkedList(5), 4)
l.printlist()

class NodeForDoublyLinkedList:
    def __init__(self, value, next = None, prev = None):
        self.prev = prev
        self.next = next
        self.value = value

class DoublyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        else:
            self.head = new_node

    def printlist(self):
        current = self.head
        list_to_print = []
        while current:
            list_to_print.append(current.value)
            current = current.next
        print(list_to_print)

    def delete_node(self, node_to_delete):
        pass
