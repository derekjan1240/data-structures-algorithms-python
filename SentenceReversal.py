def santenceReversal1(str):
    return " ".join(reversed(str.split()))

def santenceReversal2(str):
    return " ".join(str.split()[::-1])

def santenceReversal3(str):
    words = []
    length = len(str)
    spaces = [' ']

    i = 0

    while i < length:

        if str[i] not in spaces:

            word_start = i

            while i < length and str[i] not in spaces:

                i+=1
            
            words.append(str[word_start:i])
            # print(words)

        i+=1

    return " ".join(reversed(words)) 

print(santenceReversal3("   Hello world !"))