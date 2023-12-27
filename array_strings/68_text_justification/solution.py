from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        curr = []
        curr_width = 0
        for word in words:
            if not curr or curr_width + len(curr) + len(word) <= maxWidth:
                curr.append(word)
                curr_width += len(word)
            else:
                if len(curr) == 1:
                    result.append(f"{curr[0]}{' ' * (maxWidth - curr_width)}")
                else:
                    n_space = len(curr) - 1
                    w_space = (maxWidth - curr_width) // n_space
                    remainder = (maxWidth - curr_width) % n_space
                    temp = []
                    for w in curr:
                        temp.append(w)
                        if remainder > 0:
                            temp.append(" " * (w_space + 1))
                            remainder -= 1
                        else:
                            temp.append(" " * w_space)
                    temp.pop()
                    result.append("".join(temp))
                curr = [word]
                curr_width = len(word)
        temp = " ".join(curr)
        result.append(f"{temp}{' ' * (maxWidth - len(temp))}")
        return result


print(
    Solution().fullJustify(
        words=["This", "is", "an", "example", "of", "text", "justification."],
        maxWidth=16,
    )
)
