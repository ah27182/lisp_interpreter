from eval import *

# Run an interactive repl
def repl(prompt='lisp> '):
    "A prompt-read-eval-print loop."
    while True:
        val = execute(input(prompt))
        if val != None: 
            
            print(schemestr(val))
            # print(val)

# Convert experssion into normal Lisp formats
def schemestr(exp):
    "Convert a Python object back into a Scheme-readable string."
    if isinstance(exp, List):
        if exp == []:
            return '()'
        if exp[0] == "'":
            return "'" + ' '.join(map(schemestr, exp[1:]))
        else:
            return '(' + ' '.join(map(schemestr, exp)) + ')' 
    else:
        return str(exp)

repl()