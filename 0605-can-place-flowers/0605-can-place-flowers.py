# Technique usd: Single Pass Greedy Algorithm
# Time Complexity: O(M)
# Space Complexity: O(1)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:


        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                leftEmp = i==0 or flowerbed[i-1]==0
                rightEmp = i==len(flowerbed)-1 or flowerbed[i+1]==0 
                if leftEmp and rightEmp:
                    n-=1
                    flowerbed[i]=1
            if n<=0:
                return True
        return False
        