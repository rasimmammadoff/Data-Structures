class Stack:
    def __init__(self):
        self.myStack = []

    def isEmpty(self):
        return self.myStack == []

    def push(self,element):
        return self.myStack.append(element)

    def pop(self):
        if self.size() > 0:
            return self.myStack.pop()
        return "Empty Stack!"

    def peek(self):
        return self.myStack[self.size()-1]

    def size(self):
        return len(self.myStack)

    def printStack(self):
        print(self.myStack)

# test all functions
if __name__ == '__main__':
    fruits = Stack() # initialize stack 

    # push elements into stack
    fruits.push("Apple")
    fruits.push("Grape")
    fruits.push("Mango")
    fruits.push("Banana")

    print("Is my stack empty?",fruits.isEmpty())
    fruits.printStack()
    print("Last element:",fruits.peek())

    # pop elements from the stack
    print("Pop:",fruits.pop())
    print("Pop:",fruits.pop())
    print("Pop:",fruits.pop())
    print("Pop:",fruits.pop())
    print("Pop:",fruits.pop())

    print("Is my stack empty?",fruits.isEmpty())

    
