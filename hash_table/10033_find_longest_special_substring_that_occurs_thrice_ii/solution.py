import collections


class Solution:
    def maximumLength(self, s: str) -> int:
        result = 0

        char_to_count = collections.defaultdict(list)
        count = 0
        last = s[0]
        for c in s:
            if c == last:
                count += 1
            else:
                char_to_count[last].append(count)
                count = 1
                last = c
        char_to_count[last].append(count)
        for counts in char_to_count.values():
            len_1 = 0
            len_2 = 0
            len_3 = 0
            for count in counts:
                if count > len_1:
                    len_3 = len_2
                    len_2 = len_1
                    len_1 = count
                elif count > len_2:
                    len_3 = len_2
                    len_2 = count
                elif count > len_3:
                    len_3 = count
            if len_1 == len_2 and len_1 > len_3:
                len_2 -= 1

            if len_1 + len_2 + len_3 >= 3:
                result = max(result, len_1 - 2, len_2)
        if result == 0:
            return -1
        return result
