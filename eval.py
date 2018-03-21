import operator
from parse import *

# An environment: a dict of {'var': val} pairs, with an outer Env.
class Env(dict):

    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer

    # Find the innermost Env where var appears.
    def find(self, var):
        return self if (var in self) else self.outer.find(var)


# A user-defined Lisp procedure.
class Procedure(object):

    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env

    def __call__(self, *args): 
        return eval(self.body, Env(self.parms, args, self.env))

def create_op(op):

        def func(*args):

            if len(args) < 2: 
                raise TypeError("Need at least two arguments")

            total = args[0]

            for a in args[1:]:
                total = op(total, a)
            
            return total
        
        return func
    
def equals(*args):
    if len(args) < 2: 
        raise TypeError("Need at least two arguments")

    check = args[0]

    for a in args[1:]:
        if check != a:
            return False
    
    return True

def set_list(array, i, val):
    array[i] = val
    return array
def index(a,i):
    try: 
        return a[i]
    
    except IndexError as e:
        print(i,a)
        raise e
# Creating a standard enviroment for Lisp, with all the normal and speical forms assigned
def standard_env():

    env = {
        '+':create_op(operator.add),
        '-': create_op(operator.sub),
        '*': create_op(operator.mul),
        '/': create_op(operator.truediv),
        'floordiv': operator.floordiv,
        'mod': operator.mod,
        '<': lambda x,y: x < y,
        '>': lambda x,y: x > y,
        'eq?': equals,
        'or': lambda *args: any(args),
        'and': lambda *args: all(args),
        'nil': [],
        'index': index,
        'set': set_list,
        'cons': lambda x,y: (x,y),
        'car': lambda x: x[0],
        'cdr': lambda x: x[1] if isinstance(x, Dotted_List) else x[1:],
        'atom?': lambda x: isinstance(x, Number) or isinstance(x, Symbol),
        }

    return Env(env.keys(), env.values())

# Initalizing a global enviroment
global_env = standard_env()


# Evalute an expression given from the syntax tree
def eval(exp, env = global_env):

	# Variable reference
    if isinstance(exp, Symbol) and exp[0] != "'":
        return env.find(exp)[exp]

    # Numbers
    elif isinstance(exp, Number):
        return exp

    op, args = exp[0], exp[1:]

    # Quotes
    if op == 'quote' or op == "'":

        if len(args) == 1:
            return args[0]

        return args

    # Conditions
    elif op == 'cond':
        for statement in args:
            cond, conseq = statement
            if cond == 'else' or eval(cond, env):
                return eval(conseq, env)

    # Variable Defitions
    elif op == 'define':
        symbol, expr = args[0], args[1:]

        if len(expr) == 1:
            expr = expr[0]

        env[symbol] = eval(expr, env)

    # Function Creation
    elif op == 'lambda':
        params, body = args
        return Procedure(params, body, env)
    
    elif op == 'batch':
        for arg in args:
            eval(arg)
        
        return 'nil'

    # Funtion Call
    else:
        procedure = eval(op,env)

        if args != [] and args[0] == "'":
            return procedure(args[1:])

        args = [eval(arg, env) for arg in args]

        return procedure(*args)


# Parse and evaulate program in order to execute
def execute(program):
    return eval(parse(program))



