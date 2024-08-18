# Merge k Sorted Lists

You are given an array of `k` linked-lists `lists` - each linked-list is sorted
in ascending order.

Merge all the linked-lists into one sorted linked-list, and return it.


## Example 1:

**Input:** lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

**Output:** [1, 1, 2, 3, 4, 4, 5, 6]

**Explanation:** The linked-lists are:
<pre>
[
  1 -> 4 -> 5,
  1 -> 3 -> 4,
  2 -> 6
]
</pre>

Merging them into one sorted list produces:
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6


## Example 2:

**Input:** `lists = [ ]`

**Output:** `None`


## Example 3:

**Input:** `lists = [None]`

**Output:** `None`


## Constraints:
* `k == lists.length`
* <code>0 <= k <= 10<sup>4</sup></code>
* `0 <= lists[i].length <= 500`
* <code>-10<sup>4</sup> <= lists[i][j] <= 10<sup>4</sup></code>
* `lists[i]` is sorted in **ascending order**.
* The sum of `lists[i].length` will not exceed <code>10<sup>4</sup></code>

## Instructions for Running my Solution:
Requires Python 3.10 or higher.

1. Invoke the Python interpreter
2. Import the `solution.py` module
3. Instantiate the module's `Solution` class
4. Invoke the instance's `merge_k_lists` method with a `lists` argument. `lists`
   must be a list of `ListNode` and/or of `NoneType` instances.

## LeetCode Submission Detail:
See here: https://leetcode.com/submissions/detail/1359980892/
