# Technique used: Binary search
# Time complexity: O(logN) + O(logN) = O(logN)
# Space complecity: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            left, right = 0, len(nums) - 1
            first = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    first = mid
                    right = mid - 1   # keep searching LEFT
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return first

        def findLast():
            left, right = 0, len(nums) - 1
            last = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    last = mid
                    left = mid + 1   # keep searching RIGHT
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return last

        return [findFirst(), findLast()]
