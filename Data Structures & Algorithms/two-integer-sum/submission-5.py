class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Naive approach is cycle through all of the sums
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Using a hashmap/dictionary
        visits = {}
        for i in range(len(nums)):
            found = visits.get(target-nums[i])
            visits[nums[i]] = i
            if found is not None:
                indices = [i, found]
                return [min(indices), max(indices)]
