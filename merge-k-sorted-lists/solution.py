"""    
Author: Zachary Flohr    
Date: 2024-08-29  
"""    

class ListNode:    
    """A node of a singly linked list."""    
    
    def __init__(self, val: int = 0, next: 'ListNode | None' = None) -> None:
        self.val = val    
        self.next = next     
    
class Solution:    
    """A merger and sorter of sorted linked lists in a given array.
    
    Public Attributes:    
        mergeKLists: Merge all sorted linked lists in a given array
            into one sorted linked list.    
    """    
    
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        """Merge all linked lists in lists into one sorted linked list.

        Args:
            lists: A list of sorted linked lists and/or of NoneType
                instances.
        
        Returns:
            A linked list sorted in ascending order, produced from
                merging the linked lists in lists.
        """
        sorted_list = None
        for linked_list in lists:
            sorted_list = self._merge_lists(sorted_list, linked_list)
        return sorted_list
    
    def _merge_lists(self, head_a: ListNode | None,
                     head_b: ListNode | None) -> ListNode | None:
        """Merge two linked lists to produce a new, sorted linked list.

        Args:
            head_a: A sorted linked list.
            head_b: A sorted linked list.
        
        Returns:
            A new, sorted linked list produced from the merging of
                head_a and head_b.
        """
        sorted_list = ListNode()
        dummy = sorted_list
        while head_a and head_b:
            if head_a.val < head_b.val:
                sorted_list.next = head_a
                head_a = head_a.next
            else:
                sorted_list.next = head_b
                head_b = head_b.next
            sorted_list = sorted_list.next
        if head_a:
            sorted_list.next = head_a
        else:
            sorted_list.next = head_b
        return dummy.next
