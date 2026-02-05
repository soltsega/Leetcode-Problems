class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        # 1. Create a set of all integers we need to cover
        # range(left, right + 1) ensures the 'right' value is included
        target_set = set(range(left, right + 1))
        
        # 2. Create a set to collect all integers provided by the input ranges
        covered_set = set()
        for start, end in ranges:
            # We add all numbers from each interval into the covered pool
            covered_set.update(range(start, end + 1))
            
        # 3. Check if our target_set is completely contained within the covered_set
        # .issubset() returns True only if every element in target_set exists in covered_set
        return target_set.issubset(covered_set)