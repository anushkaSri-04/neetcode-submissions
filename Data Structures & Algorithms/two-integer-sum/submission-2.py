class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        seen = {}

        for i, val in enumerate(arr):
            need = target - val
            if need in seen:
                return [seen[need], i]
            seen[val] = i
