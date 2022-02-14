import convert_linked_list as converter

def reverse_linked_list(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

if __name__=="__main__":
    case1 = converter.to_linked_list([1,2,3,4,5])
    case2 = converter.to_linked_list([1,2])
    case3 = converter.to_linked_list([])

    print (f"{converter.to_list(case1)} = {converter.to_list(reverse_linked_list(case1))}")
    print (f"{converter.to_list(case2)} = {converter.to_list(reverse_linked_list(case2))}")
    print (f"{converter.to_list(case3)} = {converter.to_list(reverse_linked_list(case3))}")