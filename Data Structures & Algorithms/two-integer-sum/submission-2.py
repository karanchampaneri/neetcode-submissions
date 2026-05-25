class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## brute force solution.
        # check every single pair against target to see if it matches.

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


        #Faster Solution with a Hashmap (constant lookup time)

        seen = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen:
                return [seen[difference], i]
            seen[nums[i]] = i

            

