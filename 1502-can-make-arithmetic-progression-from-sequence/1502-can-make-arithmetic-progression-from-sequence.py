class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1]-arr[0]
        length = len(arr)-1
        for i in range(1, length):
            if abs(arr[i]-arr[i+1]) != diff:
                return False
        
        return True
        