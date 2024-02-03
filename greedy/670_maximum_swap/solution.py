class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        max_num = sorted(num_str, reverse=True)
        if num_str == max_num:
            return num

        n = len(num_str)
        indices = {n: i for i, n in enumerate(num_str)}
        for i in range(n):
            if num_str[i] != max_num[i]:
                max_idx = indices[max_num[i]]
                num_str[i], num_str[max_idx] = num_str[max_idx], num_str[i]
                break
        return int("".join(num_str))

    def maximumSwap2(self, num: int) -> int:
        digits = list(map(int, str(num)))
        # last index of digits
        last = {}
        for i, d in enumerate(digits):
            last[d] = i
        for i, d in enumerate(digits):
            # Swap the moment we find a digit bigger then the current digit and
            # is to the right of the current digit
            for k in range(9, -1, -1):
                if k <= d:
                    break
                if k in last and last[k] > i:
                    digits[i], digits[last[k]] = digits[last[k]], digits[i]
                    return int("".join(map(str, digits)))
        return num

    def maximumSwap3(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)

        # detect if num is already the maximum
        small = -1
        for i in range(n - 1):
            if digits[i] < digits[i + 1]:
                small = i
                break
        if small == -1:
            return num

        # find the rightmost largest digit
        max_i = small + 1
        max_d = digits[max_i]
        for i in range(max_i + 1, n):
            if digits[i] >= max_d:
                max_i = i
                max_d = digits[i]
        # find leftmost digit smaller than rightmost largest digit
        left = small
        for i in range(small, -1, -1):
            if digits[i] < max_d:
                left = i

        digits[left], digits[max_i] = digits[max_i], digits[left]
        return int("".join(digits))
