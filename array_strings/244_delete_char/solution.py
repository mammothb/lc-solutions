class Solution:
    """Description

    Given a string str, we should delete some characters, keep k characters in the
    string and the relative position unchanged, and minimize its lexicographic
    order, return this substring.

    @param str: the string
    @param k: the length
    @return: the substring with  the smallest lexicographic order
    """

    def delete_char(self, s: str, k: int) -> str:
        # Write your code here.
        result = []
        n = len(s)
        for i, c in enumerate(s):
            while result and result[-1] > c and n - i + len(result) > k:
                result.pop()
            result.append(c)
        return "".join(result[:k])
