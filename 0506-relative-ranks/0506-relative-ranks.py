# Technique used: Array traversal, hash map, and sorting
# Time complexity: O(N+N+NlogN+N) = O(NlogN)
# Time complexity: O(N)+O(N) O(N) = O(N)

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = {}
        a = score[::]  #O(N) space
        a.sort(reverse=True)  # O(NlogN) time
        ans = [] # O(N) space

        j = 1
        # O(N) time
        for i in range(len(a)):
            # if a[i] not in dic:
                dic[a[i]] = j
                j+=1
        # O(N) time
        for i in score:
            if dic[i]==1:
                ans.append("Gold Medal")
            elif dic[i]==2:
                ans.append("Silver Medal")
            elif dic[i]==3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(dic[i]))


        return ans

        