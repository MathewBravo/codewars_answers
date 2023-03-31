from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    allnum = []
    temp = list1
    while temp is not None:
        allnum.append(temp.val)
        temp = temp.next
    temp = list2
    while temp is not None:
        allnum.append(temp.val)
        temp = temp.next
    allnum.sort()
    if len(allnum) == 0:
        return list1
    newlist = tmp = ListNode(allnum[0])
    for num in allnum[1:]:
        tmp.next = ListNode(num)
        tmp = tmp.next
    return newlist


if __name__ == '__main__':
    list1: ListNode = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2: ListNode = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    test: ListNode = mergeTwoLists(list1, list2)
    while test is not None:
        print(test.val)
        test = test.next
