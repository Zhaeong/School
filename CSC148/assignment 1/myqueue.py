class EmptyQueueException(Exception):
    '''Exception raised when attempting to pop from an empty Stack object'''
    pass


class Queue:
    '''A first-in, first-out queue of items'''

    def __init__(self):
        '''(Queue) -> None
        A new empty Queue.'''

        self._data = []

    def enqueue(self, obj):
        '''(obj) -> None
        Place obj at the beginning of queue'''

        return self._data.append(obj)

    def dequeue(self):
        '''(Queue) -> obj
        Remove and return the top item'''

        if self.is_empty():
            raise EmptyQueueException()
        return self._data.pop(0)

    def front(self):
        '''(Queue) -> obj
        Return the top item'''

        return self._data[0]

    def is_empty(self):
        '''(Queue) -> bool
        Return whether the queue is empty.'''

        return len(self._data) == 0
