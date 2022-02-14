# Currently cant figure out how to make cyclic linked list fast but this solution works :)

import convert_linked_list as converter
def cycle_checker(head) -> bool:
        if head==None or head.next==None:  
            return False
        fast = head
        slow = head

        #btw we can use is and is not for 'None'
        while fast.next is not None and fast.next.next is not None:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                return True
        return False

# if __name__=='__main__':
#     arr1 = [3,2,0,-4]
#     pos1 = 1
#     case1 = converter.to_cyclic_linked_list(arr1,pos1)

#     arr2 = [1,2]
#     pos2 = 0
#     case2 = converter.to_cyclic_linked_list(arr2,pos2)

#     arr3 = [1]
#     pos3 = -1
#     case3 = converter.to_cyclic_linked_list(arr3,pos3)

#     print("OUTPUT\n")
#     print(f"Is {arr1} with specified position {pos1} cyclic? {cycle_checker(case1)}")
#     print(f"Is {arr2} with specified position {pos2} cyclic? {cycle_checker(case2)}")
#     print(f"Is {arr3} with specified position {pos3} cyclic? {cycle_checker(case3)}")