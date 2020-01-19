def reverse(head):

    current = head
    previous = None
    nextnode = None

    while current:

        nextnode = current.nextnode
        current.nextnode = previous

        previous = current
        current = nextnode
    
    return previous