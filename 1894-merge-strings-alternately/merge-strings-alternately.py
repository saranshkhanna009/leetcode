class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        answer = ""

        length = min(len(word1), len(word2))

        for i in range(length):
            answer += word1[i]
            answer += word2[i]

        answer += word1[length:]
        answer += word2[length:]

        return answer