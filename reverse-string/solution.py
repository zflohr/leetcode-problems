"""
Author: Zachary Flohr
Date: 2024-08-13
"""

class Solution:
    """A string reverser.

    Public attributes:
        reverseString: Reverse the characters in a list.
    """

    def reverseString(self, s: list[str]) -> None:
        """Reverse the characters in s.

        Args:
            s: An array of printable ASCII characters.

        """
        for i in range(len(s) // 2):
            char = s[i]
            s[i] = s[-1 - i]
            s[-1 - i] = char
