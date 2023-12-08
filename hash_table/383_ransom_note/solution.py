import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #  count = {}
        #  for c in magazine:
        #      if c not in count:
        #          count[c] = 1
        #      else:
        #          count[c] += 1
        count = collections.Counter(magazine)
        for c in ransomNote:
            if c not in count:
                return False
            else:
                count[c] -= 1
                if count[c] < 0:
                    return False
        return True
