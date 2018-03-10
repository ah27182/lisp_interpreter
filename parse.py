Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
Dotted_List = tuple
List = list
Exp = (Atom, List)

# Remove whitespaces and create tokens for every symbol, number, and parenthese
def tokenize(program):
    return program.replace('(',' ( ').replace(')',' ) ').split()

# Convert an atomic token to its corresponding data type 
def atomize(token):
    try:
        return Number[0](token)

    except ValueError:

        try:
            return Number[1](token)

        except ValueError:

            return Symbol(token)

# Create a syntax tree for evaluating expressions
def syntax_tree(tokens):

    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')

    token = tokens.pop(0)

    if token == '(':
        tree = []

        while tokens != [] and tokens[0] != ')':
            tree.append(syntax_tree(tokens))

        if tokens != []: 
            del tokens[0]

        return tree

    elif token == ')':
        raise SyntaxError('unexpected \')\'')

    else:
        return atomize(token)

# Parse the program by tokenizing and creating a syntax tree
def parse(program):
    return syntax_tree(tokenize(program))




