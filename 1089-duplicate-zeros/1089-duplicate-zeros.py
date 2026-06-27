class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        result = []

        for num in arr:
            result.append(num)
            if num==0:
                result.append(0)
        for i in range(len(arr)):
            arr[i]=result[i]
        