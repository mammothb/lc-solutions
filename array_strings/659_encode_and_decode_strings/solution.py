from typing import List


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs: List[str]) -> str:
        # write your code here
        n_strs = len(strs)
        result = f"{n_strs}#"
        for string in strs:
            result = f"{result}{len(string)}#{string}"
        return result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, string: str) -> List[str]:
        # write your code here'
        curr = 0
        while string[curr] != "#":
            curr += 1
        n_strs = int(string[:curr])

        result = []
        curr += 1
        start = curr
        for _ in range(n_strs):
            while string[curr] != "#":
                curr += 1
            n_string = int(string[start:curr])
            curr += 1
            result.append(string[curr : curr + n_string])
            curr += n_string
            start = curr
        return result


print(Solution().decode(Solution().encode(["we", "say", ":", "yes"])))
