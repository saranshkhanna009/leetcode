class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
       

        write = 0
        read = 0
        n = len(chars)

        while read < n:

            current = chars[read]
            count = 0

            # Count same characters
            while read < n and chars[read] == current:
                read += 1
                count += 1

            # Write character
            chars[write] = current
            write += 1

            # Write count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write 