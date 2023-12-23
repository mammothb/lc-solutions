class Solution:
    def encode(self, strs):
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        # write your code here
        num_strs = len(strs)
        lengths = [len(string) for string in strs]
        return (
            f"{num_strs}#"
            f"{''.join(f'{length}#{string}' for length, string in zip(lengths, strs))}"
        )

    def decode(self, str):
        """
        @param: str: A string
        @return: decodes a single string to a list of strings
        """
        # write your code here
        index = 0
        num_strs = 0
        while str[index] != "#":
            num_strs = num_strs * 10 + int(str[index])
            index += 1
        index += 1
        result = []
        count = 0
        while count < num_strs:
            length = 0
            while str[index] != "#":
                length = length * 10 + int(str[index])
                index += 1
            index += 1
            temp = []
            while length > 0:
                temp.append(str[index])
                length -= 1
                index += 1
            result.append("".join(temp))

            count += 1
        return result


print(Solution().decode(Solution().encode(["lint", "code", "love", "you"])))
