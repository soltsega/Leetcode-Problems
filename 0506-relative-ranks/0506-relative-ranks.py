class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = {}
        a = score[::]
        a.sort(reverse=True)
        ans = []

        j = 1
        for i in range(len(a)):
            # if a[i] not in dic:
                dic[a[i]] = j
                j+=1
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

        