class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def offer(self, item):
        self.stack1.append(item)

    def poll(self):
        if not self.stack2:  # nothing in the polling stack
            while self.stack1:  # add everything from the first stack
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()  # return the last element in the polling stack


q = Queue()


for x in range(10):
    q.offer(x)


assert q.poll() == 0
assert q.poll() == 1
assert q.poll() == 2
assert q.poll() == 3

q.offer(15)

assert q.poll() == 4
assert q.poll() == 5
assert q.poll() == 6
assert q.poll() == 7
assert q.poll() == 8
assert q.poll() == 9
assert q.poll() == 15
