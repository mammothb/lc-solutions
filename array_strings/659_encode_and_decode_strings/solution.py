from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        # write your code here
        n_strs = len(strs)
        result = f"{n_strs}#"
        for string in strs:
            result = f"{result}{len(string)}#{string}"
        return result

    def decode(self, string: str) -> List[str]:
        """
        @param: str: A string
        @return: decodes a single string to a list of strings
        """
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


class Solution2:
    def encode(self, strings):
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        # write your code here
        num_strs = len(strings)
        lengths = [len(string) for string in strings]
        return f"{num_strs}#" f"{''.join(f'{l}#{s}' for l, s in zip(lengths, strings))}"

    def decode(self, string):
        """
        @param: str: A string
        @return: decodes a single string to a list of strings
        """
        # write your code here
        index = 0
        num_strs = 0
        while string[index] != "#":
            num_strs = num_strs * 10 + int(string[index])
            index += 1
        index += 1

        result = []
        count = 0
        while count < num_strs:
            length = 0
            while string[index] != "#":
                length = length * 10 + int(string[index])
                index += 1
            index += 1

            temp = []
            while length > 0:
                temp.append(string[index])
                length -= 1
                index += 1
            result.append("".join(temp))
            count += 1
        return result


class Solution3:
    def encode(self, strings):
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        result = []
        for string in strings:
            for c in string:
                if c == "$":
                    result.append("$$")
                else:
                    result.append(c)
            result.append("$ ")
        return "".join(result)

    def decode(self, string):
        """
        @param: str: A string
        @return: decodes a single string to a list of strings
        """
        n = len(string) - 1
        i = 0
        result = []
        temp = []
        while i < n:
            if string[i] == "$":
                if string[i + 1] == " ":
                    result.append("".join(temp))
                    temp = []
                elif string[i + 1] == "$":
                    temp.append("$")
                i += 1
            else:
                temp.append(string[i])
            i += 1
        return result
