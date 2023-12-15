from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counter = {}
        max_count = 0
        max_sender = ""
        for i, sender in enumerate(senders):
            if sender not in counter:
                counter[sender] = 0
            counter[sender] += len(messages[i].strip().split(" "))
            if counter[sender] > max_count:
                max_count = counter[sender]
                max_sender = sender
            elif counter[sender] == max_count:
                if sender > max_sender:
                    max_sender = sender
        return max_sender
