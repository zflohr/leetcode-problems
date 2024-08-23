"""
Author: Zachary Flohr
Date: 2024-08-18
"""

class ListNode:
    """A node of a singly linked list."""

    def __init__(self, val = 0, next: 'ListNode | None' = None) -> None:
        self.val = val
        self.next = next

class Solution:
    """A merger and sorter of linked lists in a given array.

    Public Attributes:
        merge_k_lists: Merge all sorted linked lists in a given array
            into one sorted linked list.
    """

    def merge_k_lists(self, lists: list[ListNode | None]) -> ListNode | None:
        """Merge all linked lists in lists into one sorted linked list.

        Args:
            lists: An array of sorted linked lists and/or of NoneType
                instances.

        Returns:
            A linked list sorted in ascending order, produced from
                merging the linked lists in lists.
        """
        lists = [linked_list for linked_list in lists if linked_list]
        sorted_linked_list = None
        if len(lists):
            sorted_linked_list = lists[0]
            if len(lists) > 1:
                length = 0
                for i in range(len(lists)):
                    length += 1
                    node = lists[i]
                    while node.next:
                        length += 1
                        node = node.next
                    if i < len(lists) - 1:
                        node.next = lists[i + 1]
                merged_linked_list = lists[0]
                sorted_linked_list = self._merge_sort(merged_linked_list, length)
        return sorted_linked_list

    def _merge(self, left_head: ListNode, right_head: ListNode) -> ListNode:
        """Merge two linked lists to produce a new, sorted linked list.

        Args:
            left_head: A sorted linked list.
            right_head: A sorted linked list.

        Returns:
            A new, sorted linked list produced from the merging of
                left_head and right_head.
        """
        sorted_list = None
        if left_head == None:
            return right_head
        if right_head == None:
            return left_head
        if left_head.val <= right_head.val:
            sorted_list = left_head
            sorted_list.next = self._merge(left_head.next, right_head)
        else:
            sorted_list = right_head
            sorted_list.next = self._merge(left_head, right_head.next)
        return sorted_list

    def _merge_sort(self, head: ListNode, length: int) -> ListNode:
        """Sort the nodes of a linked list via divide and conquer.

        Args:
            head: The initial unsorted linked list or a sublist thereof
                produced by recursive calls to _merge_sort.
            length: The length of head.

        Returns:
            A sorted linked list.
        """
        if length == 1:
            return head
        middle_node = length // 2
        left_list_length = middle_node
        right_list_length = length - left_list_length
        node_count = 1
        node = head
        while node.next and middle_node > node_count:
            node_count += 1
            node = node.next
        middle_node = node
        right_list_head = middle_node.next
        middle_node.next = None
        left_list_head = self._merge_sort(head, left_list_length)
        right_list_head = self._merge_sort(right_list_head, right_list_length)
        return self._merge(left_list_head, right_list_head)
