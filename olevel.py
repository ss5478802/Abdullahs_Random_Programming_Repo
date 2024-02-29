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

"""
# Implementing Singly Linked List
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

    def printlist(self, reverse = False):
        current = self.head
        list_to_print = []
        while current:
            list_to_print.append(current.value)
            current = current.next
        print(list_to_print if reverse == False else list_to_print[::-1])

    def delete_node(self, node):
        current = self.head
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
        count = 0
        if position == 0:
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
l.delete_node(n7)
l.printlist()
l.insert_node(NodeForSinglyLinkedList(5), 1)
l.printlist()
"""
"""
# Implementing Doubly Linked List
class NodeForDoublyLinkedList:
    def __init__(self, value, next=None, prev=None):
        self.prev = prev
        self.next = next
        self.value = value


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            new_node.prev = current
            current.next = new_node
        else:
            self.head = new_node

    def printlist(self, reverse = False):
        current = self.head
        list_to_print = []
        while current:
            list_to_print.append(current.value)
            current = current.next
        print(list_to_print if reverse == False else list_to_print[::-1])

    def delete_node(self, node_to_delete):
        current = self.head
        if current.value == node_to_delete.value:
            self.head = current.next
        else:
            while current:
                if current.value == node_to_delete.value:
                    break
                else:
                    prev = current
                    current = current.next
            if current != None:
                prev.next = current.next
                if current.next != None:
                    current.next.prev = prev
                current = None

    def insert_node(self, new_node, position=None):
        current = self.head
        count = 0
        if position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif position == None:
            self.append(new_node)
        else:
            while current:
                if count == position:
                    new_node.prev = current.prev
                    current.prev.next = new_node
                    new_node.next = current
                    current.prev = new_node
                    break
                else:
                    count += 1
                    current = current.next


n11 = NodeForDoublyLinkedList(1)
n22 = NodeForDoublyLinkedList(2)
n33 = NodeForDoublyLinkedList(3)
n44 = NodeForDoublyLinkedList(4)
n55 = NodeForDoublyLinkedList(5)

ld = DoublyLinkedList(n22)
ld.append(n11)
ld.append(n44)
ld.append(n33)
ld.printlist()
ld.delete_node(n33)
ld.printlist()
ld.insert_node(n55, 1)
ld.printlist()
"""
"""
# Implementing stack using array
class StackUsingArrays:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            return self.stack.pop()
        
    def peek(self):
        if self.isEmpty():
            return "Stack is empty."
        else:
            return self.stack[-1]
        
    def size(self):
        return len(self.stack)
        

s = StackUsingArrays()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.stack)
print("Size of stack:", s.size())
s.pop()
print(s.stack)
print("Peek:", s.peek())
print("Size of stack:", s.size())
print("Stack empty:", s.isEmpty())
s.pop()
s.pop()
s.pop()
print("Stack empty:", s.isEmpty())
"""

"""
# Implementing a queue using arrays
class QueueUsingArray:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty."
        else:
            return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty."
        else:
            return self.queue[0]

    def size(self):
        return len(self.queue)


q = QueueUsingArray()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.queue)
print("Size of queue:", q.size())
q.dequeue()
print(q.queue)
print("Peek:", q.peek())
print("Size of queue:", q.size())
print("Queue empty:", q.isEmpty())
q.dequeue()
q.dequeue()
q.dequeue()
print("Queue empty:", q.isEmpty())
"""


# Implementing binary tree using nodes created using
# classes (useful if the tree is modified more often than read)


class BinaryTreeNode:
    def __init__(self, name, left=None, right=None, value=None):
        self.value = value
        self.left = left
        self.right = right
        self.name = name


def preOrderTraversal(node):
    if node != None:
        print(f"|{node.name}: {node.value}|", end="  ")
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)


def postOrderTraversal(node):
    if node != None:
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        print(f"|{node.name}: {node.value}|", end="  ")


def inOrderTraversal(node):
    if node != None:
        inOrderTraversal(node.left)
        print(f"|{node.name}: {node.value}|", end="  ")
        inOrderTraversal(node.right)


node1 = BinaryTreeNode("node1", value=10)
node2 = BinaryTreeNode("node2", value=11)
node3 = BinaryTreeNode("node3", value=9)
node4 = BinaryTreeNode("node4", value=10.5)
node5 = BinaryTreeNode("node5", value=8)
node6 = BinaryTreeNode("node6", value=13)
node7 = BinaryTreeNode("node7", value=9.5)

node1.left = node3
node1.right = node2

node2.left = node4
node2.right = node6

node3.left = node5
node3.right = node7

print("In-order traversal of the binary tree:")
inOrderTraversal(node1)
print()
print()

print("Pre-order traversal of the binary tree:")
preOrderTraversal(node1)
print()
print()

print("Post-order traversal of the binary tree:")
postOrderTraversal(node1)
print()
print()


def search(node, target):
    if node == None:
        return "Node wasn't found! Node not in tree."
    elif node.value == target:
        return f"Node found! The node was {node.name}"
    elif target > node.value:
        return search(node.right, target)
    else:
        return search(node.left, target)


print(search(node1, 9.5))

def insert(node, value):
    if node == None:
        return BinaryTreeNode(name="new_node", value = value)
    else:
        if value > node.value:
            node.right = insert(node.right, value)
        else:
            node.left = insert(node.left, value)
    return node

insert(node1, 1)
inOrderTraversal(node1)
"""
# Implementing binary tree using array
# (useful if the tree is read more often than modified)
nodes_of_binary_tree = [10, 9, 11, 8, 10, 10, 12]


def left_node(index):
    return 2 * index + 1


def right_node(index):
    return 2 * index + 2


def preOrderTraversal(index):
    if index < len(nodes_of_binary_tree):
        return (
            [nodes_of_binary_tree[index]]
            + preOrderTraversal(left_node(index))
            + preOrderTraversal(right_node(index))
        )
    else:
        return []


def inOrderTraversal(index):
    if index < len(nodes_of_binary_tree):
        return (
            inOrderTraversal(left_node(index))
            + [nodes_of_binary_tree[index]]
            + inOrderTraversal(right_node(index))
        )
    else:
        return []


def postOrderTraversal(index):
    if index < len(nodes_of_binary_tree):
        return (
            postOrderTraversal(left_node(index))
            + postOrderTraversal(right_node(index))
            + [nodes_of_binary_tree[index]]
        )
    else:
        return []


print("In-order traversal of the binary tree:")
print(inOrderTraversal(0), end="\n\n")


print("Pre-order traversal of the binary tree:")
print(preOrderTraversal(0), end="\n\n")


print("Post-order traversal of the binary tree:")
print(postOrderTraversal(0), end="\n\n")
"""
