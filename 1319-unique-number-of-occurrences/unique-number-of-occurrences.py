class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        return len(count.values()) == len(set(count.values()))