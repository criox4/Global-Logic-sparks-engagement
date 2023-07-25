def getNthFromLast(head, n):
    # Your code here
    fast = head
    slow = head
    while fast.next is not None:
        if n > 1:
            fast = fast.next
            n -= 1
        else:
            fast = fast.next
            slow = slow.next
    if n > 1:
        return -1
    return slow.data