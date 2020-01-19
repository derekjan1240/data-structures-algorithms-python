def uni_char1(s):
    return len(set(s)) == len(s)

def uni_char2(s):

    chars = set()

    for let in s:
        
        if let in chars:
            return False
        else:
            chars.add(let)

    return True

print(uni_char2('abcdee'))