from typing import List


class Solution:
    def sort(self, features: List[str], responses: List[str]) -> List[str]:
        class Feature:
            def __init__(self, name, index):
                self.name = name
                self.index = index
                self.count = 0

            def __lt__(self, other):
                if self.count == other.count:
                    return self.index > other.index
                return self.count < other.count

        counter = {}
        for i, feature in enumerate(features):
            counter[feature] = Feature(feature, i)

        for response in responses:
            response = set(response.split(" "))
            for feature in counter:
                if feature in response:
                    counter[feature].count += 1
        result = [feature.name for feature in sorted(counter.values(), reverse=True)]
        return result


print(
    Solution().sort(
        features=["cooler", "lock", "touch"],
        responses=["i like cooler cooler", "lock touch cool", "locker like touch"],
    )
)
print(
    Solution().sort(
        features=["a", "aa", "b", "c"], responses=["a", "a aa", "a a a a a", "b a"]
    )
)
