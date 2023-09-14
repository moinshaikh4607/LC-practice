def isValid(s: str) -> bool:
    stack  = []
    if len(s) <= 1 :
        return False
    
    for i in s: 
        if i in "({[":
            stack.append(i)
        else :
            if not (stack and ((stack[-1] == '(' and i == ')') or \
                (stack[-1] == '{' and i == '}') or \
                (stack[-1] == '[' and i == ']')) ):
                return False
            stack.pop()
                    
    return not stack , stack

print(isValid("(]"))
print(isValid("{[]}"))
print(isValid("]"))
print(isValid(")(){}"))
print(isValid("(])"))