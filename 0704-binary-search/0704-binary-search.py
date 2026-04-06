# TEchnique used: REcursion
# Time complexity: O(logn)
# Space complexity: O(logn)

class Solution(object):
    def search(self, nums, target):
        def helper(left, right):
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return helper(left, mid - 1)
            else:
                return helper(mid + 1, right)

        return helper(0, len(nums) - 1)