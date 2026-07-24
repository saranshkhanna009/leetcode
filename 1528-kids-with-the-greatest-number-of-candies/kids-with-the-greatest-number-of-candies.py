class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        

        maximum = max(candies)

        answer = []

        for candy in candies:

            if candy + extraCandies >= maximum:
                answer.append(True)
            else:
                answer.append(False)

        return answer