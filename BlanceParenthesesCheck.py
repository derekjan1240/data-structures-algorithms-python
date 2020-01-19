def blance_check(s):

    if len(s)%2 != 0:
        return False

    opening = set('({[')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
            
        else:
            if len(stack) == 0:
                return False
            
            # know target 
            last_open = stack.pop()

            if(last_open, paren) not in matches:
                return False

    return len(stack) == 0

print(blance_check('({(}[]))'))
print(blance_check('({}[])'))