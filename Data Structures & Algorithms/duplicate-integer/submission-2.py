class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = {}

        for i in range(len(nums)):

            if nums[i] in seen:
                return True
            
            seen[nums[i]] = i

        return False


    # ## can also use sets.

    #     if len(nums) == len(set(nums)):
    #         return False
    #     else:
    #         return True
