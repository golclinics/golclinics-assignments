import collections
def Deque():
    de = collections.deque([1,2,3])
    print("Initial deque",de)

    de.append(4)
    print("Element added from right",de)

    de.appendleft(10)
    print("Element added from left",de)

    de.pop()
    print("Element removed from right",de)

    de.popleft()
    print("Element removed from left",de)


Deque()