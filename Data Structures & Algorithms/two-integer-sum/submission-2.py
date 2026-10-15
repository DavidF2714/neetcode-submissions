from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i,n in enumerate(nums):
            difference = target - n
            if difference in _dict:
                return [_dict[difference], i]

            _dict[n] = i

        

        
        
        
