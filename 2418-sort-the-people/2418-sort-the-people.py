#Technique Used: Pairing and Sorting by key
# Time complexity: O(Nlog(N))
# Space complexity: O(N)
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # Pair names with heights
        people = list(zip(names, heights))
        
        # Sort by height in descending order
        people.sort(key=lambda x: x[1], reverse=True)
        
        # Extract and return the names
        return [name for name, height in people]