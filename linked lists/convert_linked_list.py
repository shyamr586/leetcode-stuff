class Element(object):                      #these are the elements of the linked list, each element of the 
                                    #linked lists have a value and a address to the next element which
                                    #has default value None.
                                    #this class is sometimes called Node or ListNode
    def __init__(self,value):
        self.value = value
        self.next = None

#in the below class, i use 'current' var which means it is the current element of the list.
#usually used to iterate through the ll and takes value of head at first.

def to_linked_list(lst):
    cur = dummy = Element(0)
    for e in lst:
        cur.next = Element(e)
        cur = cur.next
    return dummy.next

def to_list(ll):
    arr = []
    while ll!=None:
        arr.append(ll.value)
        ll = ll.next
    return arr

def find_element_with_index(index,original):
    head = original
    count = 0
    while head:
        if count==index:
            return head
        head=head.next
        count+=1

def to_cyclic_linked_list(lst,pos):
    cur = dummy = Element(0)
    for e in lst:
        cur.next = Element(e)
        cur = cur.next
    if pos!=-1:
        cycle_element = find_element_with_index(pos,dummy.next)
        cur.next = cycle_element
    print (to_list(dummy.next))
    # return dummy.next
