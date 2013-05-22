from stack import *
from myqueue import *
from operand import *
from shunting_yard import *


class SyntaxException(Exception):
    '''Raises an exception when the first item in a queue is not according to
    guidelines specified by the panda code, stores the token that causes
    the error'''

    def __init__(self, msg):
        self.token = msg


class InvalidExpressionException(Exception):
    '''Raises an exception when the evaluation stack is empty before the
    first value can be returned, or is not empty after the value has been
    retured'''
    pass


class NameNotFoundException(Exception):
    '''Raises an exception when a variable name specified in the panda
    code does not have a corresponding value'''
    pass


def eq(val1, val2, operator):
    '''(str,str,str)->str
    takes the string val1 and val2 and evaluates them depending of the
    string operator'''
    if operator == '+':
        return str(int(val1) + int(val2))
    elif operator == '-':
        return str(int(val1) - int(val2))
    elif operator == '/':
        return str(int(val1) // int(val2))
    elif operator == '*':
        return str(int(val1) * int(val2))


class Solver:
    '''a text document in panda code dictated by the operators var, return,
    and end, used to assign variables to infix expressions, converting
    them to postfix, and returning the solved value'''

    def __init__(self, panda_file):
        '''(Operand) -> None
        assigns the text object a value and stores it into class solver'''

        self.file = open(panda_file, 'r')
        self.eval_stack = Stack()
        self.list_of_queues = []
        self.var_dict = {}

    def parse(self):
        '''convert contents of .pnd file to a list of Queues
        return list of queues, all base-to-decimal conversions done'''

        for line in self.file:
            new_queue = Queue()
            if len(line) != 0:
                panda_line = line
                panda_line_list = panda_line.split()
                for token in panda_line_list:
                    try:
                        x = Operand(token).value()
                    except InvalidNumeralStringError:
                        new_queue.enqueue(token)
                    else:
                        new_queue.enqueue(x)
            self.list_of_queues.append(new_queue)

    def check_syntax(self):
        '''Check the first token in every Queue in the list for the syntax
        rules outlined in Line Syntax Checking. Raise a SyntaxException with
        the correct token if an error is found.'''

        list_of_lines = []
        for queue in self.list_of_queues:
            list_of_lines.append(queue.front())
        if list_of_lines[-1] != 'end':
            raise SyntaxException(list_of_lines[-1])
        for obj in list_of_lines:
            if obj not in ["var", "return", "end"]:
                raise SyntaxException(obj)
        if 'var' in list_of_lines and 'return' in list_of_lines:
            if list_of_lines.index('var') > list_of_lines.index('return'):
                raise SyntaxException('var')
        if 'return' in list_of_lines:
            if list_of_lines[-2] != 'return':
                raise SyntaxException(list_of_lines[-2])

    def run(self):
        '''Evaluates the panda file after it has been parsed and syntax
        checked. This is done by first assigning a variable to the infix
        expressions as specified in the panda file. Secondly converting
        infix expressions to postfix. Thirdly evaluating and returning
        the value'''

        for queue in self.list_of_queues:
            first_token = queue.dequeue()
            #use the first token to determine subsequent executions
            if first_token == 'var':
                variable_token = queue.dequeue()
                if not variable_token.islower():
                    raise SyntaxException(variable_token)
                elif variable_token == ('var' or 'return' or 'end'):
                    raise SyntaxException(variable_token)
                operator_token = queue.dequeue()
                if operator_token != ':=':
                    raise SyntaxException(operator_token)
                #takes rest of tokens and enqueues them
                temp_queue = Queue()
                while not queue.is_empty():
                    token = queue.dequeue()
                    if str(token) in '+-/*()' or type(token) == int:
                        temp_queue.enqueue(token)
                    elif token in self.var_dict:
                        temp_queue.enqueue(self.var_dict[token])
                    else:
                        raise NameNotFoundException()
                #convert to postfix and evaluate
                postfix_valuequeue = convert_to_postfix(temp_queue)
                while not postfix_valuequeue.is_empty():
                    q_token = postfix_valuequeue.dequeue()
                    if type(q_token) == int:
                        self.eval_stack.push(q_token)
                    elif q_token in '+-/*':
                        try:
                            one_v = self.eval_stack.pop()
                            two_v = self.eval_stack.pop()
                            self.eval_stack.push(eq(two_v, one_v, q_token))
                        except EmptyStackException:
                            raise InvalidExpressionException()
                    elif self.eval_stack.is_empty():
                        raise InvalidExpressionException()
                evalue = self.eval_stack.pop()
                self.var_dict[variable_token] = evalue
            if first_token == 'return':
                temp_queue2 = Queue()
                #takes rest of tokens and enqueues them
                while not queue.is_empty():
                    token = queue.dequeue()
                    if str(token) in '+-/*()' or type(token) == int:
                        temp_queue2.enqueue(token)
                    elif token in self.var_dict:
                        temp_queue2.enqueue(self.var_dict[token])
                    else:
                        raise NameNotFoundException()
                #convert to postfix and evaluate
                postfix_valuequeue = convert_to_postfix(temp_queue2)
                while not postfix_valuequeue.is_empty():
                    q_token = postfix_valuequeue.dequeue()
                    if type(q_token) == int:
                        self.eval_stack.push(q_token)
                    elif q_token in '+-/*':
                        try:
                            one_v = self.eval_stack.pop()
                            two_v = self.eval_stack.pop()
                            self.eval_stack.push(eq(two_v, one_v, q_token))
                        except EmptyStackException:
                            raise InvalidExpressionException()
                    elif self.eval_stack.is_empty():
                        raise InvalidExpressionException()
            if first_token == 'end':
                try:
                    end = queue.dequeue()
                    raise SyntaxException(end)
                except EmptyQueueException:
                    evalue = self.eval_stack.pop()
                    #checks if eval_stack is empty
                    if self.eval_stack.is_empty():
                        return int(evalue)
                    else:
                        raise InvalidExpressionException()

    def value(self):
        '''Return the value of the Panda file in this Solver instance.'''

        self.parse()
        self.check_syntax()
        return self.run()
