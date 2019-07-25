from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        for num in nums:
            if not result:
                result.append(str(num))
            elif "->" not in result[-1] and int(result[-1]) != num - 1:
                result.append(str(num))
            elif "->" not in result[-1] and int(result[-1]) == num - 1:
                result[-1] = "%s->%s" % (result[-1], str(num))
            
            elif "->" in result[-1]:
                if len(result[-1].split("->")) == 2 and int(result[-1].split("->")[1]) == num - 1:
                        result[-1] = result[-1].split("->")[0] + "->" + str(num)
                elif str(num) != result[-1]:
                        result.append(str(num))

        return result