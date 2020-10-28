class Queue:
    def __init__(self):
        self.myQueue = []

    def enqueue(self,element):
        return self.myQueue.append(element)
    
    def dequeue(self):
        if self.size() > 0:
            return self.myQueue.pop(0)
        return "Empty Queue!"

    def size(self):
        return len(self.myQueue)

    def isEmpty(self):
        return self.size() == 0

    def printQueue(self):
        print(self.myQueue)


if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    queue.printQueue()

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    queue.printQueue()
    print("Is queue empty?",queue.isEmpty())






            