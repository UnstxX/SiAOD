import random


class LinkedNode:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None


# Структура данных стек: реализует инициализацию, проверку на пустоту,
# добавление нового элемента в начало, извлечение элемента из начала
class Stack:
    def __init__(self):
        self.head = LinkedNode()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        if self.size > 0:
            node = LinkedNode(value)
            node.right = self.head
            self.head = node
        else:
            self.head.value = value
        self.size += 1

    def pop(self):
        if self.is_empty():
            return print("\nСтек пустой")
        remove = self.head
        if self.size > 1:
            self.head = remove.right
        self.size -= 1
        return remove.value

    def peek(self):
        if self.is_empty():
            return print("\nСтек пустой")
        return self.head.value

    def __len__(self):
        return self.size

    def reverse(self):
        current = self.head
        prev = None
        next = None

        while current is not None:
            next = current.right
            current.right = prev
            prev = current
            current = next

        self.head = prev


# Структура данных дек: реализует инициализацию, проверку на пустоту, добавление нового элемента в начало,
# добавление нового элемента в конец, извлечение элемента из начала, извлечение элемента из конца
class Deque:
    def __init__(self):
        self.head = LinkedNode()
        self.tail = self.head
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_left(self, value):
        if self.size > 0:
            node = LinkedNode(value)
            node.right = self.tail
            self.tail.left = node
            self.tail = node
        else:
            self.tail.value = value
        self.size += 1

    def push(self, value):
        if self.size > 0:
            node = LinkedNode(value)
            node.left = self.head
            self.head.right = node
            self.head = node
        else:
            self.head.value = value
        self.size += 1

    def pop_left(self):
        if self.is_empty():
            return print("\nДек пустой")
        remove = self.tail
        if self.size > 1:
            self.tail = remove.right
        self.size -= 1
        return remove.value

    def pop(self):
        if self.is_empty():
            return print("\nДек пустой")
        remove = self.head
        if self.size > 1:
            self.head = remove.left
        self.size -= 1
        return remove.value

    def peek(self):
        if self.is_empty():
            return print("\nДек пустой")
        return self.head.value

    def peek_left(self):
        if self.is_empty():
            return print("\nДек пустой")
        return self.tail.value

    def __len__(self):
        return self.size


# Задание 1
print("Задание 1:")
with open('book.txt','r') as books:
    books=open('book.txt','r',encoding="utf8")
    q1 = Deque()
    q2 = Deque()
    for book in books:
        q1.push(book)
    while not q1.is_empty():
        x = q1.pop()
        while not q2.is_empty() and q2.peek() < x:
            q1.push_left(q2.pop())
        q2.push(x)
    while not q2.is_empty():
        print(q2.pop())


# Задание 2
print("Задание 2:")
alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
random.shuffle(alphabet)
alphabet = ''.join(alphabet)
print(alphabet)
keyRing = Deque()
for letter in alphabet:
    keyRing.push(letter)

def encode(c):
    for i in range(len(keyRing)):
        x = keyRing.pop_left()
        if x == c:
            keyRing.push(x)
            val = keyRing.pop_left()
            keyRing.push(val)
            return val
        keyRing.push(x)

def decode(c):
    for i in range(len(keyRing)):
        x = keyRing.pop()
        if x == c:
            keyRing.push_left(x)
            val = keyRing.pop()
            keyRing.push_left(val)
            return val
        keyRing.push_left(x)

text = 'привет меня зовут стас'.lower()

encoded = ''
for letter in text:
    if encoded_letter := encode(letter):
        encoded += encoded_letter
    else:
        encoded += letter

print(encoded)

decoded = ''
for letter in encoded:
    if decoded_letter := decode(letter):
        decoded += decoded_letter
    else:
        decoded += letter
print(decoded)


# Задание 3
print("Задание 3:")
A = Stack()
B = Stack()
C = Stack()

disks = 4

for i in range(disks, 0, -1):
    A.push(i)

def move(a, b):
    if len(a) == 0 and len(b) > 0:
        a.push(b.pop())
    elif len(a) > 0 and len(b) == 0:
        b.push(a.pop())
    elif a.peek() > b.peek():
        a.push(b.pop())
    else:
        b.push(a.pop())

if disks % 2 == 0:
    while len(C) != disks:
        move(A, B)
        move(A, C)
        move(B, C)
else:
    while len(C) != disks:
        move(A, C)
        move(A, B)
        move(B, C)

while not C.is_empty():
    print(C.pop())


# Задание 4
print("Задание 4:")
def check_brackets(string):
    bracket_stack = Stack()
    for i in string:
        if i == '(':
            bracket_stack.push(i)
        elif i == ')':
            if bracket_stack.is_empty():
                return False
            bracket_stack.pop()
    return bracket_stack.is_empty()
with open('br.txt','r') as bracket:
    bracket = open('br.txt','r',encoding="utf8")
string = bracket.read()
print(check_brackets(string))
print(check_brackets('(()())()()()()'))


# Задание 5
print("Задание 5:")
def check_square_brackets(string):
    bracket_stack = Deque()
    for i in string:
        if i == '[':
            bracket_stack.push(i)
        elif i == ']':
            if bracket_stack.is_empty():
                return False
            bracket_stack.pop()
    return bracket_stack.is_empty()
with open('br.txt','r') as bracket:
    bracket = open('br.txt','r',encoding="utf8")
string = bracket.read()
print(check_square_brackets(string))
print(check_square_brackets('[[][][]'))


# Задание 6
print("Задание 6:")
with open('br.txt','r') as text:
    text = open('br.txt','r',encoding="utf8")
textt = text.read()

letters = Stack()
digits = Stack()
others = Stack()

for c in textt:
    if c.isalpha():
        letters.push(c)
    elif c.isdigit():
        digits.push(c)
    else:
        others.push(c)

new_text = ''

letters.reverse()
digits.reverse()
others.reverse()


while not digits.is_empty():
    new_text += digits.pop()

while not letters.is_empty():
    new_text += letters.pop()

while not others.is_empty():
    new_text += others.pop()

print(new_text)


# Задание 7
print("Задание 7:")
with open('bruh.txt','r') as bracket:
    bracket = open('bruh.txt','r',encoding="utf8")
string = bracket.read().split(" ")
numbers = []
for num in string:
    numbers.append(int(num))
deque = Deque()
for n in numbers:
    if n < 0:
        deque.push_left(n)
    else:
        deque.push(n)

while not deque.is_empty():
    x = deque.pop_left()
    if x < 0:
        deque.push(x)
    else:
        deque.push_left(x)
        break

while not deque.is_empty():
    x = deque.pop()
    if x < 0:
        print(x)
    else:
        deque.push(x)
        break

while not deque.is_empty():
    print(deque.pop_left())


# Задание 8
print("Задание 8:")
with open('book.txt', 'r') as books:
    books=open('book.txt','r', encoding='utf8')
    stack = Stack()
    for book in books:
        book = book.strip()
        print(book)
        stack.push(book)
    print()
    while not stack.is_empty():
        print(stack.pop())