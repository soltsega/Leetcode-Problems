class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing =duplicate = -1

        # Finding duplicates
        for num in nums:
            if nums[abs(num)-1]<0:
                duplicate = abs(num)
            else:
                nums[abs(num)-1] = -nums[abs(num)-1]
            
        # Finding Missing value
        for i in range(len(nums)):
            if nums[i]>0:
                missing = i+1
                break
        return [duplicate, missing]
