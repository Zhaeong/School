# Stack: an abstract data type.

# Data: a stack of values
# Operations:
#   pop: remove and return the top item.
#   is_empty: return whether the stack is empty
#   push(o): places o on top of the stack.
#   top: return top value on stack

# implementation adapted from the one developed in lecture


class EmptyStackException(Exception):
    '''Raise exception when pop method is called on an empty Stack object.'''
    pass


class Stack:
    '''A last-in, first-out (LIFO) stack of items.'''

    def __init__(self):
        '''(Stack) -> None
        A new empty Stack.'''

        self._data = []

    def pop(self):
        '''(Stack) -> object
        Remove and return the top item.'''

        if self.is_empty():
            raise EmptyStackException()
        return self._data.pop()

    def is_empty(self):
        '''(Stack) -> bool
        Return whether the stack is empty.'''

        return len(self._data) == 0

    def push(self, obj):
        '''(object) -> None
        Place obj on top of the stack.'''

        self._data.append(obj)

    def top(self):
        '''(Stack) -> object
        Return top element of stack without removing it.'''

        if not self.is_empty():
            return self._data[-1]
