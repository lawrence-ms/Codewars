# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '//' : operator.floordiv,
}

def zero(func = 0): return func if func == 0 else ops[func[0]](0, func[1])
def one(func = 1): return func if func == 1 else ops[func[0]](1, func[1])
def two(func = 2): return func if func == 2 else ops[func[0]](2, func[1])
def three(func = 3): return func if func == 3 else ops[func[0]](3, func[1])
def four(func = 4): return func if func == 4 else ops[func[0]](4, func[1])
def five(func = 5): return func if func == 5 else ops[func[0]](5, func[1])
def six(func = 6): return func if func == 6 else ops[func[0]](6, func[1])
def seven(func = 7): return func if func == 7 else ops[func[0]](7, func[1])
def eight(func = 8): return func if func == 8 else ops[func[0]](8, func[1])
def nine(func = 9): return func if func == 9 else ops[func[0]](9, func[1])

def plus(number): return ["+", number]
def minus(number): return ["-", number]
def times(number): return ["*", number]
def divided_by(number): return ["//", number]
