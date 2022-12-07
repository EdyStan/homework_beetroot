
def middle(start, last):
    if start is None:
        return None

    slow = start
    fast = start.next

    while fast != last:

        fast = fast.next
        if fast != last:
            slow = slow.next
            fast = fast.next

    return slow


# Function for implementing the Binary
# Search on linked list
def binary_search(head, value):
    start = head
    last = None

    while True:

        # Find middle
        mid = middle(start, last)

        # If middle is empty
        if mid is None:
            return None

        # If value is present at middle
        if mid.value == value:
            return mid

        # If value is more than mid
        elif mid.value < value:
            start = mid.next

        # If the value is less than mid.
        else:
            last = mid

        if not (last is None or last != start):
            break

    # value not present
    return None

