class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #brute force.
        #check i with i+1 until the end if they match?

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Quicker O(n) solution. sets/hashs?

        # seen = {}
        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return True
        #     seen[nums[i]] = i

        # return False

        #using sets.

        return len(nums) != len(set(nums))
 
