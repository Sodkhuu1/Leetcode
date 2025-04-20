import random
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
nums = [random.randrange(100) for i in range(100)]
target = int(input("Enter the target 1-150: "))
res = Solution().twoSum(nums, target)
print(res)