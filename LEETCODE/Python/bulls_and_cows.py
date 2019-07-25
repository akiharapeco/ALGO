from typing import List
from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        acount = 0
        bcount = Counter()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                acount += 1
            else:
                bcount[secret[i]]+=1
        count = 0
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                continue
            if bcount[guess[i]] > 0:
                bcount[guess[i]] -= 1
                count += 1
        return str(acount) + "A" + str(count) + "B"