from stack import *
from myqueue import *


class ParenMismatchException(Exception):
    '''Raise exception when parentheses mismatch detected in
    token_queue by convert_to_postfix.'''
    pass


def convert_to_postfix(token_queue):
    '''(Queue) -> Queue
    Take token_queue, a queue of infix-expression tokens, and convert
    tokens to postfix-expression. Return new queue of converted
    postfix-expression tokens.'''

    output_queue = Queue()
    op_stack = Stack()
    # the stack of operators

    while not token_queue.is_empty():
        item = token_queue.dequeue()

        if str(item) not in "+-*/()":
            output_queue.enqueue(item)
        # everything else would be a string

        elif item in "*/":
            while not op_stack.is_empty() and op_stack.top() in "*/":
                output_queue.enqueue(op_stack.pop())
            op_stack.push(item)
        elif item in "+-":
            while not op_stack.is_empty() and op_stack.top() in "+-*/":
                output_queue.enqueue(op_stack.pop())
            op_stack.push(item)

        elif item == "(":
            op_stack.push(item)
        elif item == ")":
            while op_stack.top() != "(":
                try:
                    output_queue.enqueue(op_stack.pop())
                except EmptyStackException:
                    raise ParenMismatchException()
            op_stack.pop()

    # no more tokens
    while not op_stack.is_empty():
        if op_stack.top() != "(":
            output_queue.enqueue(op_stack.pop())
        else:
            raise ParenMismatchException()
    return output_queue
